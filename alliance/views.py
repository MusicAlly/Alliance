from django.shortcuts import get_object_or_404, render

from alliance.models import Opportunity, UserProfile

def front_page(request):
    profile = None
    if request.user.is_authenticated():
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass
    return render(request, 'alliance/front.html', {'profile': profile})


def opportunity(request, pk):
    opp = get_object_or_404(Opportunity, pk=pk)
    return render(request, 'alliance/opportunity.html', {'opp': opp})


def user_profile(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'alliance/profile.html', {'profile': profile})
