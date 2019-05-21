<h1 align="center">Pity</h1>

<div align="center">
	<img src=misc/Logo.png width=192 />
</div>

<div align="center">
	<strong>Web apps without hosting</strong>
</div>

<div align="center">
	Part of <a href=https://github.com/Pebaz/FragmentTheory>Fragment Theory</a>.  Create pages contained entirely within a URL.
</div>


<img src=misc/EditorScreenshot.png />

### What's up with the name?

It comes from combining the name "Python" with "Itty", the first word in [Itty.Bitty](https://github.com/alcor/itty-bitty) to get "Pity".  This project was inspired by [Itty.Bitty](https://github.com/alcor/itty-bitty) but was extended to include features not included with the original.

### Quickstart

To host locally:

```bash
git clone https://github.com/Pebaz/Pity
cd Pity
python index.py
```

To host on Heroku (free tier):

```bash
# First go to https://dashboard.heroku.com/apps/<your app>/settings
# and add the "Config Var":
# KEY  VALUE
# host <your app>.herokuapp.com
git clone 
heroku git:remote -a <the app name that you went and created on Heroku>
git push heroku master
```

### About

Pity allows you to compress HTML pages (using Brotli) to a string of URL-compatible characters.  These characters are then added to a URL that you can then put in hyperlinks or paste directly into your browser to send this string of characters to wherever you decide to host Pity.  When the server receives this string, it decompresses it and returns the resulting data as HTML.  Your browser then renders the HTML to display what was essentially an entire webpage contained within a URL.

Using [Itty.Bitty](https://github.com/alcor/itty-bitty), the amount of bytes of data you can place into a single page is limited.  With Pity, there is no limit because a choice of using a route instead of a URL fragment is given to you within the editor.  This allows you to create large HTML pages and then compress them into a URL without fear of running out of bytes in the fragment.

A valid question could be raised about the motivation of creating a similar project that removes said limit.  The exact reason for creating Pity arose for the need to allow pages stored within URLs (that are not hosted anywhere) to be able to send each other arbitrary data within the URL fragment.  If I were to use [Itty.Bitty](https://github.com/alcor/itty-bitty), this is impossible.  Hence the need for Pity.

A perfect companion for Pity is [Fragment Theory](https://github.com/Pebaz/FragmentTheory), a JavaScript library that enables the transfer of JSON data between static HTML pages.  It can even be used on offline HTML pages!

As you can see, the combination of Pity + Fragment Theory = static pages that can be dynamic!

In addition, since the generated URLs can be excessively long, the use of a URL shortener is in order.  This is precisely the reason I created [Concise](https://github.com/Pebaz/Concise).  With the combination of Pity + Fragment Theory + Concise, you could create a web of shareable hyperlinks that contain a full site ***without needing to pay for hosting, setup your own servers, or deal with server-side code!***

### Routes

* `GET: /<data>` Converts the URL fragment into an HTML page. Optionally expects a path instead for near unlimited data within the URL.

* `GET: /edit`Editor to create Pity sites

* `POST: /render` Expects JSON body with the compressed data within the "value" key:

* ```json
  { "value" : "G5sB4..." }
  ```

### Templates

Any file in the `templates` directory will show up in the editor as predefined page stubs for you to work off of.  Feel free to flesh them out and send me a pull request!  ;)