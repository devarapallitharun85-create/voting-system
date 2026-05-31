from django.shortcuts import render, get_object_or_404, redirect
from .models import Election, Candidate, Vote
from django.contrib.auth.decorators import login_required

def home(request):
    elections = Election.objects.all()
    candidates = Candidate.objects.all()

    return render(request, 'home.html', {
        'elections': elections,
        'candidates': candidates
    })

@login_required
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    already_voted = Vote.objects.filter(
        voter=request.user,
        candidate__election=candidate.election
    ).exists()

    if already_voted:
        return render(request, 'message.html', {
            'message': 'You have already voted in this election.'
        })

    Vote.objects.create(
        voter=request.user,
        candidate=candidate
    )

    return redirect('/')

def results(request):
    candidates = Candidate.objects.all()

    return render(request, 'results.html', {
        'candidates': candidates
    })