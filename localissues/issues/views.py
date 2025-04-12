from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Issue
from .forms import IssueForm
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    """Finds all question papers"""
    issues = Issue.objects.all()
    return render(
        request, 'lir/index.html', {
            'issues': issues
    })

@login_required(login_url="/login/")
def create_issue(request):
    issues = Issue.objects.all()
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/issues/thanks/')
    else:
        form = IssueForm()

    return render(request, 'lir/create-issue.html', {'form': form})


@login_required(login_url="/login/")
def show_all(request):
    issues = Issue.objects.all()
    return render(request, 'lir/issues.html', {'issues':issues} )

@login_required(login_url="/login/")
def show_issue(request, issue_pk):
    print(request)
    issue = Issue.objects.filter(pk=issue_pk)
    return render(request, 'lir/issue.html', {'issue': issue} )

@login_required(login_url="/login/")
def delete_issue(request, issue_pk):
    issue = Issue.objects.filter(pk=issue_pk).delete()

    return HttpResponseRedirect('/issues/thanks/')
@login_required(login_url="/login/")
def thanks(request):
    return render(request, 'lir/thanks.html', {'thanks': 'thanks', })