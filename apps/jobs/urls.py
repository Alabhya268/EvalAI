from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r"^challenge/(?P<challenge_pk>[0-9]+)/"
        r"challenge_phase/(?P<challenge_phase_pk>[0-9]+)/submission/(?P<submission_pk>[0-9]+)$",
        views.change_submission_data_and_visibility,
        name="change_submission_data_and_visibility",
    ),
    url(
        r"^challenge/(?P<challenge_id>[0-9]+)/"
        r"challenge_phase/(?P<challenge_phase_id>[0-9]+)/submission/$",
        views.challenge_submission,
        name="challenge_submission",
    ),
    url(
        r"^(?P<challenge_pk>[0-9]+)/" r"remaining_submissions/$",
        views.get_remaining_submissions,
        name="get_remaining_submissions",
    ),
    url(
        r"^submissions/(?P<submission_pk>[0-9]+)/re-run-by-host/$",
        views.re_run_submission_by_host,
        name="re_run_submission_by_host",
    ),
    url(
        r"^challenge_phase_split/(?P<challenge_phase_split_id>[0-9]+)/leaderboard/$",
        views.leaderboard,
        name="leaderboard",
    ),
    url(
        r"^phase_split/(?P<challenge_phase_split_pk>[0-9]+)/public_leaderboard_all_entries/$",
        views.get_all_entries_on_public_leaderboard,
        name="get_all_entries_on_public_leaderboard",
    ),
    url(
        r"^submission/(?P<submission_id>[0-9]+)$",
        views.get_submission_by_pk,
        name="get_submission_by_pk",
    ),
    url(
        r"^challenge/(?P<challenge_pk>[0-9]+)/update_submission/$",
        views.update_submission,
        name="update_submission",
    ),
    url(
        r"^challenges/(?P<challenge_pk>[0-9]+)/update_partially_evaluated_submission/$",
        views.update_partially_evaluated_submission,
        name="update_partially_evaluated_submission",
    ),
    url(
        r"^challenge/(?P<challenge_pk>[0-9]+)/submission/$",
        views.get_submissions_for_challenge,
        name="get_submissions_for_challenge",
    ),
    url(
        r"^queues/(?P<queue_name>[\w-]+)/$",
        views.delete_submission_message_from_queue,
        name="delete_submission_message_from_queue",
    ),
    url(
        r"^challenge/queues/(?P<queue_name>[\w-]+)/$",
        views.get_submission_message_from_queue,
        name="get_submission_message_from_queue",
    ),
    url(
        r"^submission_files/$",
        views.get_signed_url_for_submission_related_file,
        name="get_signed_url_for_submission_related_file",
    ),
    url(
        r"^leaderboard_data/(?P<leaderboard_data_pk>[0-9]+)/$",
        views.update_leaderboard_data,
        name="update_leaderboard_data",
    ),
    url(
        r"^challenge/(?P<challenge_pk>[0-9]+)/eks_bearer_token/$",
        views.get_bearer_token,
        name="get_bearer_token",
    ),
    url(
        r"^phase_splits/(?P<challenge_phase_split_pk>[0-9]+)/teams/(?P<participant_team_pk>[0-9]+)/github_badge/$",
        views.get_github_badge_data,
        name="get_github_badge_data",
    ),
    url(
        r"^phases/(?P<challenge_phase_pk>[0-9]+)/send_submission_message/(?P<submission_pk>[0-9]+)/$",
        views.send_submission_message,
        name="send_submission_message",
    ),
    url(
        r"^phases/(?P<challenge_phase_pk>[0-9]+)/submission_count_by_status/$",
        views.challenge_phase_submission_count_by_status,
        name="challenge_phase_submissions_by_status",
    ),
    url(
        r"^phases/(?P<challenge_phase_pk>[0-9]+)/get_submission_file_presigned_url/$",
        views.get_submission_file_presigned_url,
        name="get_submission_file_presigned_url",
    ),
    url(
        r"^phases/(?P<challenge_phase_pk>[0-9]+)/finish_submission_file_upload/(?P<submission_pk>[0-9]+)/$",
        views.finish_submission_file_upload,
        name="finish_submission_file_upload",
    ),
    url(
        r"^submission/(?P<submission_pk>[0-9]+)/update_started_at/$",
        views.update_submission_started_at,
        name="update_submission_started_at",
    ),
    url(
        r"^challenges/(?P<challenge_pk>[0-9]+)/"
        r"submissions/(?P<submission_pk>[0-9]+)/update_submission_meta/$",
        views.update_submission_meta,
        name="update_submission_meta",
    ),
]

app_name = "jobs"
