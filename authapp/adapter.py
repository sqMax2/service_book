from allauth.account.adapter import DefaultAccountAdapter


class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    """
    Adapter to disable allauth new signups
    Used at service_book/settings.py with key ACCOUNT_ADAPTER
    """

    def is_open_for_signup(self, request):
        """
        Checks whether the site is open for signups.
        """
        return False
