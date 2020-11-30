from django.contrib.auth.models import User
from django.core.management import BaseCommand

from book.models import Book
from user_profile.models import Profile


class Command(BaseCommand):
    help = 'Creating db to deploy'

    @staticmethod
    def create_user_with_profile(username: str,
                                 email: str,
                                 firstname: str,
                                 lastname: str,
                                 password: str,
                                 is_librarian: bool):
        user_object = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                               last_name=lastname)
        profile_object = Profile(user=user_object, is_librarian=is_librarian, is_student=(not is_librarian))

        user_object.save()
        profile_object.save()

    @staticmethod
    def add_book(name: str):
        Book(in_use_by=None,
             name=name,
             info='info about the book').save()

    def handle(self, *args, **options):
        emails_data = ['shang@gmail.com',
                       'rhialto@outlook.com',
                       'alastair@yahoo.com',
                       'rnelson@live.com',
                       'dgriffith@hotmail.com',
                       'stakasa@msn.com',
                       'papathan@yahoo.com',
                       'bflong@hotmail.com',
                       'mglee@yahoo.ca',
                       'mcast@gmail.com',
                       'rfisher@msn.com',
                       'dmbkiwi@mac.com']
        names_data = ['Felicia Medrano',
                      'Pixie Partridge',
                      'Leslie Benson',
                      'Cairon Roy',
                      'Mariana Woodley',
                      'Harriet Gonzales',
                      'Doris Boyd',
                      'Kajol Merrill',
                      'Sherri Cisneros',
                      'Debra Smyth']
        usernames_data = [
            'airplane',
            'instinctive',
            'stage',
            'intend',
            'bottle',
            'bustling',
            'wicked',
            'downtown',
            'aloof',
            'modern',
            'ocean',
            'coast',
        ]

        for i in range(len(names_data)):
            first_name, last_name = names_data[i].split()
            self.create_user_with_profile(username=usernames_data[i],
                                          email=emails_data[i],
                                          firstname=first_name,
                                          lastname=last_name,
                                          password='asdf123!',
                                          is_librarian=False)

        book_names = [
            'Отцы и дети',
            'Дубровский',
            'Капитанская доска',
            'Евгений Онегин',
            'Герой нашего времени',
            'Война и мир',
            'На дне',
            'Гроза',
            'Преступление и наказание',
            'Гранатовый браслет',
            'Горе от ума',
            'Мцыри',
            'Ася',
            'Обломов',
            'Собачье сердце',
            'Письма о добром и прекрасном',
            'Уроки французского',
            'Человек на часах',
        ]

        for book_name in book_names:
            self.add_book(book_name)