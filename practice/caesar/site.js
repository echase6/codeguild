'use strict';
/**
 * Returns string encrypted by moving each letter ahead in alphabet by key.
 *
 * Assumes characters are upper-case.
 * All non-letters are preserved as-is (assumming they are punctuation)
 *
 * @type {String}
 */
function caesarEncrypt(plainStr, key) {
  var encryptedText = '';
  for (var i = 0; i < plainStr.length; i += 1) {
    var charVal = plainStr[i].charCodeAt();
    var aCharCode = 'A'.charCodeAt();
    var zCharCode = 'Z'.charCodeAt();
    if (charVal >= aCharCode && charVal <= zCharCode) {
      var encCode = (charVal - aCharCode + key) % 26 + aCharCode;
      encryptedText += String.fromCharCode(encCode);
    } else {
      encryptedText += plainStr[i];
    }
  }
  return encryptedText;
}

/**
 * Returns string decrypted by moving each letter back in alphabet by key.
 *
 * Since decryption is encryption in-reverse, this calls the encryption
 * algorithm with the key shifted backward.
 *
 * @type {String}
 */
function caesarDecrypt(encStr, key) {
  var decKey = 26 - key;
  var plainText = caesarEncrypt(encStr, decKey);
  return plainText;
}


var inString = 'HELLO, THERE.';
console.dir(inString);
var outString = caesarEncrypt(inString, 10);
console.dir(outString);
var retString = caesarDecrypt(outString, 10);
console.dir(retString);
