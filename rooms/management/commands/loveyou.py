from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "this command that this loves me "

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="how many times do you want me to tell you that i love you"
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("i love you"))
