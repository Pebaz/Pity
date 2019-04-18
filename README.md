# Pity
Part of [Fragment Theory]().  Create pages contained entirely within a URL.

### Routes

* `GET: /<data>` Converts the URL hash into an HTML page. Optionally expects a path instead for near unlimited data within the URL.

* `GET: /edit`Editor to create Pity sites

* `POST: /render` Expects JSON body with the compressed data within the "value" key:

* ```json
  { "value" : "G5sB4..." }
  ```



### Note

This project was inspired by [Itty.Bitty.Site](https://github.com/alcor/itty-bitty) but was extended to include features not included with the original.







* Clear button
* Show check if good and then fadeOut
* Preview with Modal + Iframe
* Different HTML templates (Bulma, NES.css, etc.)

```
<iframe style="display: inline-flex; width: 90%; height: 90%; margin: 0" src="http://red-lang.org"></iframe>
```

