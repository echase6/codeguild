'use strict';

/**
 *  Constructor Color holds RBG numbers and has two methods:
 *  blend() -- blends and returns a new color based on original and passed one
 *  toHex() -- returns string representing RGB values in Hex.
 */
function Color(r, g, b) {
  this.red = r;
  this.green = g;
  this.blue = b;
}

var colorProto = {
  blend: function(color) {
    var r1 = Math.floor((this.red + color.red) / 2);
    var g1 = Math.floor((this.green + color.green) / 2);
    var b1 = Math.floor((this.blue + color.blue) / 2);
    return new Color(r1, g1, b1);
  },
  toHex: function() {
    var redDigits = ('0' + this.red.toString(16)).slice(-2);
    var greenDigits = ('0' + this.green.toString(16)).slice(-2);
    var blueDigits = ('0' + this.blue.toString(16)).slice(-2);
    var outHex = '#' + redDigits + greenDigits + blueDigits;
    return outHex;
  }
};


Color.prototype = colorProto;

var red = new Color(255, 0, 0);
var blue = new Color(0, 0, 255);
var purple = red.blend(blue);
var redInHex = red.toHex();

console.dir(purple);
console.dir(purple.toHex());
console.dir(redInHex);
