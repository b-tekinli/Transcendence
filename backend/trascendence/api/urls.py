from django.urls import path, include
from django.views.generic.base import RedirectView
from trascendence.api.views import AuthView
from trascendence.api.views import InteractionsView
from trascendence.api.views import TorunamentsView
from trascendence.api.views import Uploads

# Write decorator to restrict http methods for requests
# auth_redirect -> 42/oauth -> auth/token/code -> page

urlpatterns = [

    # Authentication
    path('auth/sign-in/42', AuthView.sign_in_42),
    path('auth/sign-in', AuthView.sign_in),
    path('auth/sign-up', AuthView.sign_up),
    path('auth_redirect', AuthView.OAuth),
    path('auth/token/code', AuthView.token),

    # Interactions
    path('interacts/friends', InteractionsView.get_friends),
    path('interacts/friends/add', InteractionsView.add_friend),
    path('interacts/friends/delete/<user>', InteractionsView.delete_friend),
    path('interacts/invitation>', InteractionsView.get_invitations),
    path('interacts/invitation/<invite_code>/accept', InteractionsView.accept_invitation),
    path('interacts/invitation/<invite_code>/delete', InteractionsView.decline_invitation),
    path('interacts/blacklist', InteractionsView.get_blacklist),
    path('interacts/blacklist/add', InteractionsView.add_blacklist),
    path('interacts/blacklist/<target_username>/delete', InteractionsView.remove_blacklist),

    # Tournaments
    path('tournaments/invitations', TorunamentsView.get_tournament_invitations),
    path('tournaments/invitations/<invitationcode>', TorunamentsView.get_tournament_invitation),
    path('tournaments/invitations/<invitationcode>/accept', TorunamentsView.accept_tournamet),
    path('tournaments/invitations/<invitationcode>/delete', TorunamentsView.decline_tournament),
    path('tournaments/', TorunamentsView.get_tournaments),
    path('tournaments/user', TorunamentsView.get_tournaments_for_user),
    path('tournaments/<tournamentcode>', TorunamentsView.get_tournament),
    path('tournaments/<tournamentcode>/matches', TorunamentsView.get_tournament_matches),
    path('tournaments/create', TorunamentsView.create_tournament),
    path('tournaments/<tournamentcode>/<username>/delete', TorunamentsView.remove_tournament_user),

    # Uploads
    path('uploads/upload', Uploads.upload_file),
    path('uploads/delete/<file>', Uploads.delete_file)
]
