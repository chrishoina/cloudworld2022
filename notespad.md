# Time Sheet

1. **09.29.2022 - 1:02:05**
    * What I did:
        * Found datasets, loaded them into my ADB REST-enabled the tables. Created a directory for the Flask app. Created an initial app, copied some Bootstrap. Researched making a request with the [Fetch API](https://flask.palletsprojects.com/en/2.2.x/patterns/javascript/#making-a-request-with-fetch)

    * What I need to-do:
        * Create drop downs by year, and then by dimension
        * Create a separate "take the happiness quiz" html file
        * Create a table for the happiness quiz (HAPPY2022) ✅
        * Auto-REST enable the table ✅

2. **09.30.2022 - 3:10:28**
    * What I did:
        * Got the parallax function to work on the main page, almost ready for the dropdown items for the REST APIs.
        * Added images to index page

    * What I need to do:
        * Should just select by year, then populate a dropdown for country
            * Put the contents into a table
        * Need to finish the quiz page:
            * Desc of the test
            * 2x ladders for the questions
            * Submit to POST
            * Message Flash with successful post
        * Need to add in Learn more:
            * Gallup article on [methodology](https://news.gallup.com/poll/122453/understanding-gallup-uses-cantril-scale.aspx)
            * [World Happiness Report](https://worldhappiness.report/)

```javascript
   <div id="geology-fact">
        {{ include "geology_fact.html" }}
    </div> -->
<script>
    const geology_url = {{ url_for("geology_fact")|tojson }}
    const geology_div = getElementById("geology-fact")
    fetch(geology_url)
        .then(response => response.text)
        .then(text => geology_div.innerHtml = text)
</script>
```
