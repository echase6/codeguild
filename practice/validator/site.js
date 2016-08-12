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
 * displayInvalid() highlights the input box and un-hides the warning message.
 */
function displayInvalid(entryItem) {
  entryItem.addClass('invalid');
  $(entryItem).next().addClass('visible-warning');
}

/**
* displayValid() un-highlights the input box and hides the warning message.
 */
function displayValid(entryItem) {
  entryItem.removeClass();
  $(entryItem).next().removeClass();
}
/**
 * Check whether the input string is a match and changes class to invalid if not
 * @param  {jQuery selector} entryItem The selector on the form for an input
 * @param  {reg exp} regExp            Regular expression to test the match
 *         Return true if there is a match, false otherwise.
 */
function runValidator(entryItem, regExp) {
  var entryString = getFieldEntry(entryItem);
  if(stringValidator(entryString, regExp)) {
    displayValid(entryItem);
    return true;
  } else {
    displayInvalid(entryItem);
    return false;
  }
}

/**
 * Main Name validator, for the name entry on the form.
 *
 * Matches only for strings that are correctly typed up to the last character.
 */
function runNameValidator() {
  var nameEntryItem = $('#name-input');
  var nameRegExp = /^[a-z]*(\s[a-z]*)?$/i;
  runValidator(nameEntryItem, nameRegExp);
}

/**
 * Main Date of Birth validator, for the DoB entry on the form.
 *
 * Matches only for strings that are correctly typed up to the last character.
 */
function runDobValidator() {
  var dobEntryItem = $('#dob-input');
  var dobRegExp = /^\d{0,4}$|^\d{4}-\d{0,2}$|^\d{4}-\d{2}-\d{0,2}$/;
  runValidator(dobEntryItem, dobRegExp);
}

/**
 * Main Phone number validator, for the Phone Num entry on the form.
 *
 * Matches only for strings that are correctly typed up to the last character.
 */
function runPhoneValidator() {
  var phoneEntryItem = $('#phone-input');
  var phoneRegExp = /^\d{0,3}$|^\d{3}-\d{0,3}$|^\d{3}-\d{3}-\d{0,4}$/;
  runValidator(phoneEntryItem, phoneRegExp);
}

/**
 * runFinalNameChecker() checks to see if the entered name is valid.
 *
 * Returns boolean, true if entire name is valid.
 */
function runFinalNameChecker() {
  var nameEntryItem = $('#name-input');
  var nameRegExp = /^[a-z]+\s[a-z]+$/i;
  return runValidator(nameEntryItem, nameRegExp);

}

/**
 * runFinalDobChecker() checks to see if the entered date is valid.
 *
 * Returns boolean, true if entire DoB is valid.
 */
function runFinalDobChecker() {
  var dobEntryItem = $('#dob-input');
  var dobRegExp = /^\d{4}-\d{2}-\d{2}$/;
  return runValidator(dobEntryItem, dobRegExp);
}

/**
 * runFinalPhoneChecker() checks to see if the entered phone # is valid.
 *
 * Returns boolean, true if entire phone number is valid.
 */
function runFinalPhoneChecker() {
  var phoneEntryItem = $('#phone-input');
  var phoneRegExp = /^\d{3}-\d{3}-\d{4}$/;
  return runValidator(phoneEntryItem, phoneRegExp);
}

/**
 * runFinalFormValidator() checks all entries in the form and displays
 *   the appropriate banner.
 */
function runFinalFormValidator() {
  if (runFinalNameChecker() &
      runFinalDobChecker() &
      runFinalPhoneChecker()) {
    $('h2').text('Successful form submission!');
    $('h2').attr('class', 'successful');
  } else {
    $('h2').text('Unsuccessful form submission!');
    $('h2').attr('class', 'unsuccessful');
  }
}

/**
 * Event Handler registrator.
 */
function registerEventHandlers() {
  $('#name-input').on('keyup', runNameValidator);
  $('#dob-input').on('keyup', runDobValidator);
  $('#phone-input').on('keyup', runPhoneValidator);
  $('form').on('submit', function(event) {
    event.preventDefault();
    runFinalFormValidator();
  });
}

$(document).ready(registerEventHandlers);
