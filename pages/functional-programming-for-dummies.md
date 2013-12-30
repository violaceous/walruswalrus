published: true
title: Functional Programming for Dummies
date: 12-30-2013
tags: [functional programming, javascript, underscore] 

A few months back I did the exercises that my company uses during developer interviews to see if I could still hack it and also to establish that they really weren't too difficult. One of them involved writing some code to represent a deck of cards that would be able to shuffle and deal the cards. They were looking for an Object Oriented solution but for whatever reason that really didn't feel right to me. In the days of old I wrote a poker server and client in Java as well as a program to generate an exact odds table for texas hold 'em poker using all the fancy combinatorics I learned at college. In both instances I represented cards as integers rather than objects. A card really just represents a value and creating an object for that seemed like overkill, but I couldn't really articulate anything beyond that at the time.

Recently I've been reading [Functional Javascript](http://www.amazon.com/Functional-JavaScript-Introducing-Programming-Underscore-js-ebook/dp/B00D624AQO/ref=sr_1_1?ie=UTF8&qid=1388441201&sr=8-1&keywords=functional+javascript) by Michael Fogus. For fun. I even stopped in the middle of the Michael Chabon novel I'm reading to read this book instead. I am starting to feel like I'm getting my groove back. Lately when developing, or when reading this book, I feel like I understand what is going on rather than having to use trial and error to figure out what is going on. There are a lot of moving parts in when trying to use these modern MVC javascript frameworks but I'm starting to get it down. 

One of the guys that I work with recently wrote up the cards problem in Javascript using an Object Oriented style. He doesn't have the strong OO background that CS grads get fed as he is a self-taught developer so he used it as a practice exercise. And thinking about that after reading some of this book made me want to do the same thing only utilizing functional programming instead. Reading this book has helped refresh how much more enjoyable aspects of this can be so I wanted to actually write something to stretch the ol' programming muscles.

This [fiddle](http://jsfiddle.net/violaceous/F5Gv9/) is the result. I'm sure it could be better written in general, and I'm sure it could be more functional in style, but it works and I'm content with it. I omitted deal (the cards are stored as an array, so just pop one off to deal) and focused on the presentation of the cards and the shuffling. 

I represented the cards by the numbers 0 through 51. To determine the suit I divide by 13 and to determine the rank I use modulo 13. I then look those numbers up using underscore's where with lists I made that map the numbers to values. I use underscore's map function to be able to transform the array of numbers to an array of string descriptions of the cards such as "Ace of Spades".

I wrote the shuffle to try to emulate a rifle shuffle. It would have been a lot easier to do a recursive shuffle that what it was passed in two and then randomly chose the order to reassemble them, but trying to do a rifle shuffle let me create more functions to mess around with. For the rifle shuffle I split the deck in two with one function and passed it to a merge function that took the two halves and an empty result array. This function recursively loops through taking a card from each half of the deck that was passed in and adding them in a random order to the result array.
 
    function mergeCards(right, left, merged) {
        if (right.length === 0 || left.length === 0) {
            return merged.concat(right.concat(left));
        } else {
            merged = merged.concat(combineTwoCards([right.pop()], [left.pop()]));
            return mergeCards(right, left, merged);
        }
    }

Not the most exciting thing in the world, but it let me practice a bit.  
