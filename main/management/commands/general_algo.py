# coding: utf-8
from django.core.management.base import BaseCommand
from main.algorithms import general_algo


class Command(BaseCommand):
    help = '123'

    def handle(self, *args, **options):
        general_algo()
