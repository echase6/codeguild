'use strict';

var encKey = 10;
var distroEnglish = {A: 73, B: 9, C: 30, D: 44, E: 130, F: 28, G: 16, H: 35,
  I: 74, J: 2, K: 3, L: 35, M: 25, N: 78, O: 74, P: 27, Q: 3, R: 77,
  S: 63, T: 93, U: 27, V: 13,	W: 16, X: 5, Y: 19, Z: 1};

/**
 * Determines whether a letter is A-Z, inclusive
 *
 * @param  {String}  char Single character string
 * @return {Boolean} True if it is A-Z, inclusive
 */
function isLetter(char) {
  var aCharCode = 'A'.charCodeAt();
  var zCharCode = 'Z'.charCodeAt();
  var charVal = char.charCodeAt();
  return charVal >= aCharCode && charVal <= zCharCode;
}

/**
 * rotateLetter shifts the letter by encKey (global variable), something
 * which I don't like but is necessary to make the _.map() function work.
 *
 * @param  {String} char The letter to be rotated
 * @return {String}      The shifted letter (or not, if not a letter.)
 */
function rotateLetter(char) {
  var aCharCode = 'A'.charCodeAt();
  var charVal = char.charCodeAt();
  if (isLetter(char)) {
    var encode = (charVal - aCharCode + encKey) % 26 + aCharCode;
    var outChar = String.fromCharCode(encode);
  } else {
    outChar = char;
  }
  return outChar;
}

/**
 * Returns string encrypted by moving each letter ahead in alphabet by key.
 *
 * Assumes characters are upper-case.
 * All non-letters are preserved as-is (assumming they are punctuation)
 *
 * @type {String}
 */
function caesarEncrypt(plainStr) {
  var encryptedText = _.map(plainStr, rotateLetter);
  return encryptedText.join('');
}

/**
 * Returns string decrypted by moving each letter back in alphabet by key.
 *
 * Since decryption is encryption in-reverse, this calls the encryption
 * algorithm with the key shifted backward (had to modify global variable
 * encKey to make that work, however.)
 *
 * @type {String}
 */
function caesarDecrypt(encStr) {
  encKey = 26 - encKey;
  var plainText = caesarEncrypt(encStr);
  return plainText;
}

/**
 * Returns the Chi-Squared value for the two string distributions, shifted
 * by the element key.
 *
 * @param  {object} distEng      Letter distribution of the English Language
 * @param  {object} distEncrypt  Letter distribution in the encrypted msg
 * @param  {integer} shift       The shift amount to apply to distEncrypt
 * @return {float}               The Chi-Squared value
 */
function computeChiSquare(distEng, distEncrypt, shift) {
  var chiSum = 0;
  var aCharCode = 'A'.charCodeAt();
  for (var letter in distEng) {
    var letterCode = letter.charCodeAt() - aCharCode;
    var testLet = String.fromCharCode((shift + letterCode) % 26 + aCharCode);
    if (!_.isUndefined(distEncrypt[testLet])) {
      chiSum += Math.pow(distEncrypt[testLet], 2) /
        distEng[letter];
    }
  }
  return chiSum;
}

/**
 * Find the letter distribution in the encrypted text.
 *
 * @param  {string} encStr The encrypted test
 * @return {object}        The letter distribution of the input text.
 */
function getDistroEncrypt(encStr) {
  var distroEncrypt = _.countBy(encStr);
  return distroEncrypt;
}


/**
 * Calculate the most likely key that decrypts the message.
 *
 * Relies on Enclish lanuage letter distribution.
 *
 * @param  {string} encStr  Encrypted message
 * @param  {object} distEng Letter distribution
 * @return {integer}         Most likely key
 */
function guessKey(encStr, distEng) {
  var keyList = {};
  var distEncrypt = getDistroEncrypt(encStr);
  for (var i = 0; i < 26; i += 1) {
    keyList[i] = computeChiSquare(distEng, distEncrypt, i);
  }
  var guessedKey = _.sortBy(_.toPairs(keyList),
    function(o) {return o[1];})[0][0];
  return guessedKey;
}

var inString = 'THIS TEXT IS LONG ENOUGH TO FIND OUT THE ENCRYPTION KEY.';

console.dir(inString);
var outString = caesarEncrypt(inString);
console.dir(outString);
var retString = caesarDecrypt(outString);
console.dir(retString);
var guessedKey = guessKey(outString, distroEnglish);
console.dir(guessedKey);
