'use strict';

/**
 * Completer object contains completions.
 *
 * completions will have keys as the completion and values as weights.
 */
function Completer() {
  this.completionsToWeights = {};
}

var modifyCompleter = {
  /**
   * addCompletion adds a completion to the completions container, in-place
   *   The weighting defaults to 1 (i.e., this is the initial weight.)
   * @param {string} str the string to be added to the completions list
   */
  addCompletion: function(str) {
    if (typeof this.completionsToWeights[str] === 'undefined') {
    this.completionsToWeights[str] = 1;
    }
  },
  /**
   * removeCompletion() removes a completion from the container (in-place)
   * @param  {string} str the string to be removed from the completions list.
   */
  removeCompletion: function(str) {
    delete this.completionsToWeights[str];
  },
  /**
   *complete() returns an array of completions, highest weighted first
   * @param  {string} prefix The prefix to match to.
   * @return {list of strings}  A list of strings that match the prefix.
   */
  complete: function(prefix) {
    var matchPattern = RegExp('^' + prefix);
    var matchesToWeights = _.pickBy(this.completionsToWeights,
      function(weight, completion) {return matchPattern.test(completion);});
    var matchesWeights = _.toPairs(matchesToWeights);
    var orderedMatchesWeights = _.orderBy(matchesWeights,
      function(o) {return o[1];}, 'desc');
    var orderedMatches = _.map(orderedMatchesWeights,
      function(o) {return o[0];});
    return orderedMatches;
  },
  /**
   * selectCompletion() increases the weight of a given completion (in-place)
   * @param  {string} str The prefix that was matched.
   */
  selectCompletion: function(str) {
    this.completionsToWeights[str] += 1;
  }
};

Completer.prototype = modifyCompleter;

var textCompleter = new Completer();

textCompleter.addCompletion('eric');
textCompleter.addCompletion('google');
textCompleter.addCompletion('dolly');
textCompleter.removeCompletion('eric');
textCompleter.addCompletion('dollar');
textCompleter.selectCompletion('dolly');
textCompleter.selectCompletion('dolly');


var matches = textCompleter.complete('dol');
console.dir(matches);
