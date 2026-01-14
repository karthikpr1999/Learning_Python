def solve (N, start, finish, Ticket_cost):
    """
        N => number of tram stations
        
        arrangement of Ticket_cost =>
        tram stations list [1, 2, 3, 4]
        ticket cost of tram station 1 to tram station 2 => cost(1->2)
        and also ticket cost of tram station 2 to tram station 1 => cost(1->2)
        [cost(1->2), cost(2->3), cost(3->4), cost(1->4)]
    """
    station_one, station_two = sorted((start, finish))
    route_one_cost = sum(Ticket_cost[(station_one - 1) : (station_two - 1)])
    another_route_cost = sum(Ticket_cost) - route_one_cost
    return sorted((route_one_cost, another_route_cost))[0]
 
N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))
 
out_ = solve(N, start, finish, Ticket_cost)
print (out_)