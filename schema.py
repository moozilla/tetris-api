"""Define GraphQL schema for WWC rankings endpoint"""

from graphene import ObjectType, String, Int, List  # ID, Boolean, Field
from api import get_sprint_rankings

# JSON example:
# {
#   "warning":"",
#   "error":"",
#   "rankings":[
#     {
#       "rank":1,
#       "username":"Vince_HD",
#       "country":"Philippines",
#       "score":16771
#     },
#     {
#       "rank":2,
#       "username":"Woojung03",
#       "country":"Malaysia",
#       "score":18290
#     }
#   ]
# }


class Ranking(ObjectType):
    """Represents all the info from the `rankings` JSON field"""

    rank = Int()
    username = String()
    country = String()
    score = Int()


class Query(ObjectType):
    """Query the rankings endpoint."""

    # count = how many to return (0 for all?)
    # start = where in rankings to start (default 1)
    rankings = List(Ranking, count=Int(required=True), start=Int(required=False))

    def resolve_rankings(self, _, count, start=None):
        """Resolver for rankings query."""
        api_result = get_sprint_rankings(count, start)
        print(api_result.rankings)
        return api_result.rankings
