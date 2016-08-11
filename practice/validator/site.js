'use strict';

function nameValidator(testString) {
  // var nameRegExp = new RegExp('[a-zA-Z]+(\s[a-zA-Z]*){0,1}');
  var nameRegExp = /^[a-zA-Z]*(\s[a-zA-Z]*){0,1}$/;
  return nameRegExp.test(testString);
}

function dobValidator(testString) {
  var dobRegExp = /^\d{0,4}(\-\d{0,2}){0,1}$/;
  return dobRegExp.test(testString);
}

function phoneValidator(testString) {
  var phoneRegExp = /^\d{0,3}(\-\d{0,3}(\-\d{0,4})){0,1}$/;
  return phoneRegExp.test(testString);
}

function showInvalidEntry(entryItem) {
  entryItem.addClass('invalid');
}

function getFieldEntry(entryItem) {
  return entryItem.val();
}

function runNameValidator() {
  var nameEntryItem = $('#name-input');
  var nameString = getFieldEntry(nameEntryItem);
  if (!nameValidator(nameString)) {
    showInvalidEntry(nameEntryItem);
  } else {
    nameEntryItem.removeClass();
  }
}

function runDobValidator() {
  var dobEntryItem = $('#dob-input');
  var dobString = getFieldEntry(dobEntryItem);
  if (!dobValidator(dobString)) {
    showInvalidEntry(dobEntryItem);
  } else {
    dobEntryItem.removeClass();
  }
}

function runPhoneValidator() {
  var phoneEntryItem = $('#phone-input');
  var phoneString = getFieldEntry(phoneEntryItem);
  if (!phoneValidator(phoneString)) {
    showInvalidEntry(phoneEntryItem);
  } else {
    phoneEntryItem.removeClass();
  }
}


function registerEventHandlers() {
  $('#name-input').on('keyup', runNameValidator);
  $('#dob-input').on('keyup', runDobValidator);
  $('#phone-input').on('keyup', runPhoneValidator);
}

$(document).ready(registerEventHandlers);
