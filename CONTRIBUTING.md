## To help modify/add the content

1. Fork this repo.
2. Leave a comment at the issue you are going to work on. If no existed issue matches, create a new one.
3. Submit pull request.


## To proofread the content

Directly comment in the source.
If serious changes require, create a new issue.


## Content style guide

### Source naming rule
The source for `http://tw.pycon.org/2015apac/en/foo/bar-baz` should be at `<repo>/en/foo-bar_baz.html`.
Mind the `-` and `_` conversion.

### Use absolute URL path
For simplicity, use absolute URL path, that is, the url path including `/2015apac/<lang>/...`.
(relative path will be converted by TinyMCE anyway)

For example, a link to page `http://tw.pycon.org/2015apac/en/foo/bar`, use

```html
<a href="/2015apac/en/foo/bar">...</a>
```
