# Week 13 Deliverables (E9) - Due 4/19/16
For this week make sure that you have completed the following:
* Fork Assignment 10 to your own github repository.
    * You can access assignment 10 [HERE](https://github.com/Geospatial-Python/assignment_10)
* Clone the repository locally
* Note that TravisCI is still turned off for this weel

## Deliverable
1. In the `io_geojson` module write a function that ingests the twitter data and returns a dictionary.  Note that you could write this from scratch or, if a suitable library exists (maybe a built-in), utilize someone else's library.
1. Create a new Tweet class or extend the existing Point class to store:
    * The tweet text
    * The tweet spatial information, e.g. lat/lon coordinats (be careful with how twitter ships the data (lat/lon vs. lon/lat)
    * A few (3-5) other interesting tweet attributes
    
    Note: Here I leave it entirely to you to decide whether the Point class should be extended to include tweet information, a Tweet class should be created that inherets from the Point class, or a Tweet class should be created that contains (composition) a Point object.
    * As a comment to your PR, please let me know how you implemented the Point - Tweet relationship and why.  A sentene or two is plenty.
1. Ensure that the GUI that you created last week is taking the form of a class.  This will ensure that you can track state more easily.  See above or [here](http://zetcode.com/gui/pyqt4/firstprograms/) for an example of what I mean by, 'the form of a class' (under the heading 'An Application Icon', the `class Example()` code block).
1. Once your current GUI window is a class extend it to:
    * Have a QWebView act as a the main, central widget.
    * Embed a Folium map into the QWebView
    * Add the tweet location markers to the Folium map
        * As above, the bounding box tweets will need to be randomly located within the bounding box.
    * Add an open button or file menu item.  This will open a [`QtGui.QFileDialog`](http://zetcode.com/gui/pyqt4/dialogs/).  Using this dialog, the user can supply a file of tweets and those tweets are drawn on the map.  Ideally, your window loads a blank map centered on a default location.  When the user loads a file of tweets, the markers are drawn and the window recenters to the mean center of the points.  This will require reloading the HTML in the `QWebView`.  If you struggle with this, you can simply not draw the map until the tweets are opened, and hard code the centering to Phoenix.
    
    Hint: The folium map object has a `__repr__` magic method that returns the map as raw HTML.  The `QWebView` has a method [`setHtml()`](http://pythoncentral.io/pyside-pyqt-tutorial-qwebview/), as well as a method [`reload()`](http://pyqt.sourceforge.net/Docs/PyQt4/qwebview.html#reload).  I was not able to get `reload()` to properly redraw and instead had to make a second call to `setHtml()`.
1. Include a screen shot (png, jpg) of your GUI in the PR.  Please keep these small (resize to 700px width would be ideal).  Git does not like large, binary files.
