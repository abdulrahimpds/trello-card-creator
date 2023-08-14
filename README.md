# Trello Card Creator Assignment

This repository contains two distinct implementations of a Trello Card Creator: one built with Python using Flask and another with Node.js using Express.

## Overview

This a simple web application that allows users to input specific details and, upon submission, a card is created in Trello with the provided information.

## Implementations

### Python (Flask) Version

 - This version uses Flask as its web framework and makes HTTP requests to the Trello API to create cards.

### Node.js (Express) Version

 - This version utilizes the Express framework and employs the axios package to make HTTP requests to the Trello API.

## Setting Up Trello Power-Up for API Key and Token

1. Visit https://glitch.com/@trello.
2. Locate and select "trello-power-up".
3. Click on "View Source", followed by "Remix".
4. After remixing, note the new project name and copy its URL.
5. Navigate to https://trello.com/power-ups/admin to create a new Power-Up.
6. Fill in the required fields: `Iframe connector URL (Required for Power-Up)`, `Email`, `Support contact`, and `Author`.
7. Paste the URL you copied in step 4 into the `Iframe connector URL (Required for Power-Up)` field.
8. Proceed to the `API Key` section of the `Power-Up`.
9. Generate and copy the `API Key`. Then, click on `Token` (adjacent to the API Key description), grant the required permissions by clicking Allow, and copy the generated token.

## Usage

1. Navigate to the desired version's directory (either Trello API - Python or Trello API - NodeJS).
2. Once the application is running, access the web interface via your browser, fill in the form with the desired card details, and submit.
3. A confirmation message will be displayed upon successful card creation or an error message otherwise.

## Assignment Context

This project was developed as an assignment during my internship at Cloudify. It was designed to assess my skills in API calls, backend development, and my proficiency with both Node.js and Python. Through this assignment, I've demonstrated the ability to create a similar application using two different tech stacks, showcasing adaptability and versatility in software development.
