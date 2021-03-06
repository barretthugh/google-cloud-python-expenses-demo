from setuptools import find_packages
from setuptools import setup

setup(
    name='gcloud-expenses-demo',
    version='0.1',
    description='Expense report upload (example for gcloud-python)',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gcloud',
        'Sphinx',
    ],
    extras_require = {
        'web': [
            'pyramid',
            'pyramid_chameleon',
            'waitress',
        ]
    },
    entry_points={
        'console_scripts': [
            'submit_expenses = gcloud_expenses.scripts.submit_expenses:main',
            'review_expenses = gcloud_expenses.scripts.review_expenses:main',
            'expense_receipts = gcloud_expenses.scripts.expense_receipts:main',
        ],
        'paste.app_factory': [
            'main = gcloud_expenses.webapp:main',
        ],
    },
)
