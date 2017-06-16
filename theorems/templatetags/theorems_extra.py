from django import template

register = template.Library()

@register.simple_tag
def proof_index(proof):
    return proof.theorem.sorted_proof_set.index(proof) + 1
