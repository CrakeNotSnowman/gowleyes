

# ROADMAP: Gowleyes Documents to Epub version Alpha 0.0.00
Future expansions are considered in this file. 
Their presence is not a promise that they'll exist, but rather this file serves as an
early outline of features this project hopes to add, as well as changes in directions


The format is adapted from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
It wont adhere perfectly, but it's a start. 


Dates follow YYYY-MM-DD format


> “What do you think?” he demanded impetuously.

> “About what?” He waved his hand toward the book-shelves.

> “About that. As a matter of fact you needn’t bother to ascertain. I ascertained. They’re real.”

> “The books?”

> He nodded.

> “Absolutely real — have pages and everything. I thought they’d be a nice durable cardboard. Matter of fact, they’re absolutely real. Pages and — Here! Lemme show you.”

> Taking our scepticism for granted, he rushed to the bookcases and returned with Volume One of the “Stoddard Lectures.”

> “See!” he cried triumphantly. “It’s a bona-fide piece of printed matter. It fooled me. This fella’s a regular Belasco. It’s a triumph. What thoroughness! What realism! Knew when to stop, too — didn’t cut the pages. But what do you want? What do you expect?”

-- Owl Eyes in Great Gatsby by F. Scott Fitzgerald


## [0.0.00] 2019-XX-XX
Completed.
### Contributors
Keith Murray

email: kmurrayis@gmail.com |
twitter: [@keithTheEE](https://twitter.com/keithTheEE) |
github: [CrakeNotSnowman](https://github.com/CrakeNotSnowman)

Unless otherwise noted, all changes by @kmurrayis

### Short Term Roadmap

Trying to make more use of my kindle, I want to convert more documents to a kindle friendly format. 

This will be more of a pipeline than a single unified project. And as such will rely on a lot of other programs 

research citation check mendeley:

Build in time with testing

#### Add
 - LaTex to html
    * [X] Using htlatex: it's ... not the solution I plan on using honestly. It has trouble with equations
 - html to epub
 - html to MOBI
 - Jupyter Notebook to html
 - PDF to LaTex
    This is going to be the worst one of my early goals, hands down. And it should probably get it's own project. The steps will probably be focused on blocking out the pdf, Identifying specific elements, (Title info, page specific headers and footers, figure blocks, column text) and order the blocks in a tex file. 
 - latexml: add that and make install notes
#### Change
 - On arxiv vanity--Get it to handle failed to render issues, also wait for rendering, worst case I learn of a useful selenium feature that I don't need in this project

#### Deprecate
#### Remove
#### Fix
#### Security
#### Documentation
#### Consider
#### Testing

---

### General to Long Term Expansion

#### Add The ability to call from the Browser 
##### Pairing with chrome/firefox extension
[X] Turns out this was manageable without an extreme amount of work
When on webpage, clicking the extension should auto format for epub/MOBI and send to the kindle to read later. The extension needs to grow and be built out so the user can interact with it, (auto send on left click, adjust settings on right click, etc) but for now it 'kind of works'. 

##### Working with a flask server
[X] In a simple form, this is already up and running. There should be more work done on it, but hey I can press a FF/Chrome extension and recieve an ebook on my kindle. 


#### Machine Learning for Formatting
One of the few areas I think can readily and tangibly benifit from machine learning in this project over rules based methods. 
 - [Linear Digressions](http://lineardigressions.com/episodes/2018/2/4/auto-generating-websites-with-deep-learning) Episode on the topic
 - [Blog Post](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/) on the topic

I've got a feeling mapping pdf's to latex (and perhaps to html and ebooks) can be greatly enhanced by the uses of an neural net. Notes on this may be extended in a sepperate project. 

