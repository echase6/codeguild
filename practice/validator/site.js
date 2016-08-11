'use strict';
/**
 * Tests whether the string matches the regular expression
 * @param  {string} testString The string to test
 * @param  {reg exp} regExp    The regular expression.  Not a string.
 * @return {boolean}           True if there is a match, false otherwise.
 */
function stringValidator(testString, regExp) {
  return regExp.test(testString);
}

/**
 * The the string entered on the form.
 * @param  {jQuery selector} entryItem The selector for a text input.
 * @return {string}                    The string entered on the form.
 */
function getFieldEntry(entryItem) {
  return entryItem.val();
}

/**
 * Check whether the input string is a match and changes class to invalid if not
 * @param  {jQuery selector} entryItem The selector on the form for an input
 * @param  {reg exp} regExp            Regular expression to test the match
 */
function runValidator(entryItem, regExp) {
  var entryString = getFieldEntry(entryItem);
  if(!stringValidator(entryString, regExp)) {
    entryItem.addClass('invalid');
  } else {
    entryItem.removeClass();
  }
}

/**
 * Main name validator, for the name entry on the form.
 */
function runNameValidator() {
  var nameEntryItem = $('#name-input');
  var nameRegExp = /^[a-z]*(\s[a-z]*)?$/i;
  runValidator(nameEntryItem, nameRegExp);
}

/**
 * Main Date of Birth validator, for the DoB entry on the form.
 */
function runDobValidator() {
  var dobEntryItem = $('#dob-input');
  var dobRegExp = /^\d{0,4}$|^\d{4}-\d{0,2}$|^\d{4}-\d{2}-\d{0,2}$/;
  runValidator(dobEntryItem, dobRegExp);
}

/**
 * Main Phone number validator, for the Phone Num entry on the form.
 */
function runPhoneValidator() {
  var phoneEntryItem = $('#phone-input');
  var phoneRegExp = /^\d{0,3}$|^\d{3}-\d{0,3}$|^\d{3}-\d{3}-\d{0,4}$/;
  runValidator(phoneEntryItem, phoneRegExp);
}
/**
 * Event Handler registrator.
 */
function registerEventHandlers() {
  $('#name-input').on('keyup', runNameValidator);
  $('#dob-input').on('keyup', runDobValidator);
  $('#phone-input').on('keyup', runPhoneValidator);
}

$(document).ready(registerEventHandlers);
