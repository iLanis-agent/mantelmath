(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }
  var EAR = 15, CORBEL_SPAN = 60;

  function mantelPlan(openingCm) {
    if (!(openingCm > 0)) return { error: "the opening must be positive" };
    var shelf = round1(openingCm + 2 * EAR);
    var verdict;
    if (openingCm < 90) verdict = "a petite fireplace";
    else if (openingCm <= 130) verdict = "a standard fireplace";
    else verdict = "a grand fireplace";
    return { shelf: shelf, verdict: verdict };
  }

  function corbelPlan(shelfCm) {
    if (!(shelfCm > 0)) return { error: "the shelf must be positive" };
    var corbels = Math.max(2, Math.ceil(shelfCm / CORBEL_SPAN));
    var spacing = round1(shelfCm / (corbels - 1));
    var verdict;
    if (corbels === 2) verdict = "a pair of corbels";
    else verdict = "a row of corbels";
    return { corbels: corbels, spacing: spacing, verdict: verdict };
  }

  function legPlan(bottomCm, shelfThickCm) {
    if (!(bottomCm > 0) || !(shelfThickCm > 0)) return { error: "the shelf bottom and the shelf thickness must be positive" };
    if (shelfThickCm >= bottomCm) return { error: "the shelf is thicker than its height" };
    var leg = round1(bottomCm - shelfThickCm);
    var verdict;
    if (leg < 90) verdict = "a low mantel";
    else if (leg <= 120) verdict = "a classic mantel";
    else verdict = "a tall mantel";
    return { leg: leg, verdict: verdict };
  }

  function renderMantel(r, openingCm) {
    return "An opening " + openingCm + " cm wide takes a labeled " + r.shelf + " cm shelf with " + EAR + " cm ears - " + r.verdict + ".";
  }

  function renderCorbel(r, shelfCm) {
    return "A shelf " + shelfCm + " cm takes " + plural(r.corbels, "corbel") + " at " + r.spacing + " cm centers - " + r.verdict + ".";
  }

  function renderLeg(r, bottomCm, shelfThickCm) {
    return "A shelf bottom at " + bottomCm + " cm with a labeled " + shelfThickCm + " cm shelf takes legs " + r.leg + " cm tall - " + r.verdict + ".";
  }

  var api = { mantelPlan: mantelPlan, corbelPlan: corbelPlan, legPlan: legPlan, renderMantel: renderMantel, renderCorbel: renderCorbel, renderLeg: renderLeg };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.MantelMath = api;
})(this);
