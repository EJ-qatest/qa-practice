# QUESTION-001: Can a customer order more than one of the same product?

**Type:** Requirements question (not a defect)

## Observation
With `standard_user`, clicking **Add to cart** switches the button to **Remove**. The cart always shows quantity **1** and offers no way to change it.

## Question for the product owner
Is "one of each item per order" intended? If customers should be able to buy multiple units, the cart needs a quantity control.

## Why I raised it as a question
The behavior is consistent and deliberate-looking, and no requirement I had access to covered quantity. Logging it as a bug would assume the intent - asking first avoids a wasted fix or a missed feature.
