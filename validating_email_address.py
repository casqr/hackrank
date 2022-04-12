"""You are given an integer N followed by N  email addresses. Your task is to print a list containing only valid
email addresses in lexicographical order.Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores [a-z],[A-Z],[0-9],[_-]
The website name can only have letters and digits [a-z],[A-Z],[0-9]
The extension can only contain letters [a-z].[A-Z]
The maximum length of the extension is 3"""


def fun(s):

    if '@' in s and '.' in s and s.count('@') < 2:
        username = s.split('@')[0]
        website = s.split('@')[1].split('.')[0]
        extension = s.split('@')[1].split('.')[1]

        if username.isidentifier() or '-' in username and website.isalnum() and extension.isalpha():
            if len(extension) <= 3 and '_' not in website:
                return True
        else:
            return False
    else:
        return False
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
