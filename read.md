PC Builder App
This is a web application for building custom PCs. To run the application, you will need to follow the instructions below.

Installation
Clone the repository to your local machine:


git clone https://github.com/username/pc-builder.git
cd pc-builder/
Install the required Python packages:


pip install -r requirements.txt
Import the PostgreSQL database dump file:

pg_restore -U username -d pcpiyasa pcpiyasa.dump

Note: Replace username and database_name with your PostgreSQL username and the name of the database where you want to import the dump file.

Set the PostgreSQL database password in the settings:


# pc_builder/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pcpiyasa',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # <-- set your PostgreSQL password here
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
Run the Django development server:


python manage.py runserver
The application should now be running at http://localhost:8000/.

Usage
You can use the PC Builder web application to build custom PCs by selecting various components such as processors, motherboards, graphics cards, and more. Once you have added components to your build, you can save your build or purchase the components directly from the website.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.