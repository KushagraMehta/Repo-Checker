from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .form import user_name
import requests
import json
from threading import Thread


class home_page(TemplateView):
    template_name = "WELCOME_PAGE/index.html"

    def get(self, request):
        user_name_form = user_name()
        return render(request, self.template_name, {'form': user_name_form})

    def post(self, request):
        user_name_data = user_name(request.POST)

        if user_name_data.is_valid():
            print(user_name_data.cleaned_data['user'])
            return HttpResponseRedirect('user/'+str(user_name_data.cleaned_data['user']))
        else:
            print("______________Error______________________")
            print(user_name_data.errors)
            return render(request, self.template_name, {'form': user_name_data})


class repo_explorer(TemplateView):

    template_name = "USER_PAGE/index.html"
    commit_data = []
    count_data = []

    def commiter(self, repo):
        commits = []
        count = []
        counter = 0
        r = requests.get('https://api.github.com/repos/' +
                         self.username+'/'+repo+'/commits')
        commits_json = json.loads(r.text)

        if 'message' not in commits_json:
            for i in commits_json:
                datetime = i['commit']['committer']['date']
                datetime = " ".join(datetime[:-1].split('T'))
                if not commits:
                    commits.append(datetime)
                    counter += 1
                elif commits[-1] == datetime:
                    counter += 1
                else:
                    commits.append(datetime)
                    count.append(counter)
                    counter = 0
            self.commit_data.append(commits)
            self.count_data.append(count)

    def get(self, request, username=None):
        self.username = username
        r = requests.get('https://api.github.com/users/' +
                         self.username+'/repos')
        repos_json = json.loads(r.text)
        repos = []
        # if 'limit exceeded' in repos_json['message']:
        #     raise Exception("API Limmit Exceeded. Plz wait for 1 Day.. ;-)")

        for i in repos_json:
            if i['fork'] == False:
                repos.append(i['name'])

        repo_thead = []
        for repo in repos:
            repo_thead.append(Thread(target=self.commiter, args=(repo,)))
            repo_thead[-1].start()

        for thread in repo_thead:
            thread.join()
        print(self.commit_data)
        graph = {'username': self.username, 'repo_data': json.dumps(
            repos), "commit_data": json.dumps(self.commit_data), "count_data": json.dumps(self.count_data)}
        return render(request, self.template_name, graph)
