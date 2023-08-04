# Time Sheet

1. **09.29.2022 - 1:02:05**
    * Did:
        1. Found datasets, loaded them into my ADB REST-enabled the tables. Created a directory for the Flask app. Created an initial app, copied some Bootstrap. Researched making a request with the [Fetch API](https://flask.palletsprojects.com/en/2.2.x/patterns/javascript/#making-a-request-with-fetch)

    * To-do:
        1. Create drop downs by year, and then by dimension
        2. Create a separate "take the happiness quiz" html file
        3. Create a table for the happiness quiz (HAPPY2022) ✅
        4. Auto-REST enable the table ✅

2. **09.30.2022 - 3:10:28**
    * Did:
        * Got the parallax function to work on the main page, almost ready for the dropdown items for the REST APIs.
        * Added images to index page

    * To-do:
        1. Should just select by year, then populate a dropdown for country
            * Put the contents into a table
        2. Need to finish the quiz page:
            * Desc of the test
            * 2x ladders for the questions
            * Submit to POST
            * Message Flash with successful post
        3. Need to add in Learn more:
            * Gallup article on [methodology](https://news.gallup.com/poll/122453/understanding-gallup-uses-cantril-scale.aspx)
            * [World Happiness Report](https://worldhappiness.report/)
3. **10.01.2022 - 2:30:00**
    * Did:
        * Cleaned up the index html; including fixing the parallax feature
        * Added a card and button to test the submit function (for a `GET` request to the tables)
        * Read up on Jinja2 templates (specifically `Include` ), Bokeh documentation, the JS Fetch API

    * To-do:
        1. Button to trigger function for collecting data from tables, and then producing a chart
            * Just do by country and then populate one chart on the page
            * Can we use `f Strings` to pass in the different URLs (like in the Folium documentation)?
        2. Figure out a way to dynamically pass that to the html page without reloading
        3. Finish the take quiz + `POST` page
            * Need to figure out message flashing as well (for user feedback)

4. **10.02.2022 - 1:30:00**
    * Did:
        1. I was able to render Bokeh chart in `Index` page
        2. I continued to familiarize myself with the `include` statement in Jinja
        3. I'm trying to better understand the `url for()` function in Flask
        4. Worked through the `GET` request workflow (in the ordsendpoints.py file)
            * To start, I'm going to limit selection by country and only return a single year. Once that is complete, I will extend to include all other years
            * Also, is pagination an issue? Do I need to account for that? 

    * To-do:
        1. Need to finish the happiness quiz page
            * But also need to make the `POST` request work 
            * Need to include message flashing for when a `POST` is successful

    



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
