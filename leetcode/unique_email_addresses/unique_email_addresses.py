class Solution(object):
    def replace_dots(self, email):
        at = email.find('@')

        return email[:at].replace('.', '') + email[at:]

    def ignore_after_plus(self, email):
        at = email.find('@')
        plus = email.find('+')

        return email[:plus] + email[at:]

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        destination_emails = set([])

        for email in emails:
            proc_email = self.ignore_after_plus(email)
            proc_email = self.replace_dots(proc_email)

            destination_emails.add(proc_email)

        return len(destination_emails)