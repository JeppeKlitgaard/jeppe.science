---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: experience

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 20

title: 📃 Experience
subtitle: _Among other things - Have a peek at my CV for more!_

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
experience:
  - title: R&D Engineering
    company: Nanonord A/S
    company_url: 'http://nanonord.dk/'
    company_logo: nanonord
    location: Aalborg, Denmark
    date_start: '2022-06-01'
    # date_end: '2022-11-01'
    description: |
      Research and Development role in Nuclear Magnetic Resonance (NMR) sensor company
      combining mechanical engineering, physics, and software engineering skills.

      Majority of work focused on development of a testing and shimming platform for a
      $≈ 1T$ permanent magnet Halbach cylinder using high-precision Hall Effect sensors and
      NMR frequency data in order to improve passive shimming outcomes and improve the internal
      magnetic field homogeneity.

      The primary product, the Tveskaeg system, uses NMR relaxometry methods to determine isotope
      content and derived quantities on liquid phase samples.
      Use-cases include salt content determination in food industries,
      boron concentration determination in water desalination plants,
      and many other industrial cases.

      _Currently on leave to finish academic studies._

  - title: Summer Research Internship
    company: Cavendish Laboratory, University of Cambridge
    company_url: 'https://www.phy.cam.ac.uk/'
    company_logo: uni_of_cam
    location: Cambridge, United Kingdom
    date_start: '2021-06-01'
    date_end: '2021-09-01'
    description: |
      __10-week summer internship at University of Cambridge.__
      
      Work focused on development of a physical and simulated cartpole experiment by the name of <a href="https://jeppeklitgaard.github.io/CartER/" target="_blank">CartER</a>.

      `CartER` enables reproducable investigation of model-free and model-based reinforcement learning
      algorithms using a standardised interface that integrates with the
      <a href="https://stable-baselines3.readthedocs.io/en/master/" target="_blank">`stable-baselines3`</a> project.

      Primarily `PPO` and `A2C` were investigated using long-running physical experiments.

      Supervisors:

      - <a href="http://people.bss.phy.cam.ac.uk/~pc245/" target="_blank">Professor Pietro Cicuta</a> (Department of Physics)
      - <a href="https://www.cl.cam.ac.uk/~pl219/" target="_blank">Professor Pietro Liò</a> (Department of Physics)

  - title: Software Engineering Intern
    company: Intropic Limited
    company_url: 'https://intropic.io/'
    company_logo: intropic_io
    location: London, United Kingdom
    date_start: '2020-06-01'
    date_end: '2020-09-01'
    description: |
      __8-week summer internship in a London-based FinTech startup.__

      Introduced and authored a variety of Python projects dealing with REST API development,
      data processing and created a streaming data pipeline in Kafka/Faust.
      Collaborated on existing client-facing API’s.

  - title: Substitute Teacher
    company: Ans & Grauballe Skole
    company_url: 'https://silkeborg.dk/'
    company_logo: silkeborg_kommune
    location: Silkeborg, Denmark
    date_start: '2018-01-01'
    date_end: '2019-09-01'
    description: |
      __Fixed temporary position in Ans Skole’s Special Education section.__

      Previously worked as a regular substitute teacher in the public school section.
      Primarily taught Natural Sciences, English and Mathematics, ages 13 – 16.

design:
  columns: '2'
---
