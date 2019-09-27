<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://api.loones.es/">
    <img src="images/loones.jpg" alt="Logo" >
  </a>

  <h3 align="center">API Loones</h3>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Update Changes in Production](#update-changes-in-production)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework (DRF)](https://www.django-rest-framework.org)
* [Celery - Periodic Tasks](http://www.celeryproject.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites



### Installation


### Update changes in Production

Follow the next steps in order to up to date the API loones in Procuction server:

1. Access to the Production Server (Note to Carlos: `server_loones`)
2. Go to folder that contains the APILoones code:  `cd <folder-path>`
3. Get all the new changes from the repository. `git pull`
4. Rewrite the user-permissions to the APILoones files `chown -R www-data:www-data <folder-path>`
5. Finally Run. `npm run build` (for ChartsLoones) 

#### Note:
* `folder-path` could be the following paths:
    * `/CODE/loones` (Prestashop)
    * `/CODE/APILoones` (API)
    * `/CODE/ChartsLoones` (Dashboard)

#### Example (Screenshot):
<p align="center">
    <img src="images/production-up-to-date.png" alt="Production Up to Date" >
</p>

#### Mega command: 

```bash
    cd /CODE/loones && git pull && chown -R www-data:www-data /CODE/loones 
```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact
Rafael García - rafa@loones.es <br>
Carlos García - carlos@loones.es

Project Link: [https://github.com/loones19/APILoones](https://github.com/loones19/APILoones)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[production-up-to-date]: images/production-up-to-date.png
