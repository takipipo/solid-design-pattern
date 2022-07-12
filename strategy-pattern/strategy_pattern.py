import string
import random

from typing import List
from abc import abstractmethod, ABC


def generate_id(length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class ProcessStrategyInterface(ABC):
    @abstractmethod
    def create_ordering(self, list_tickets: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOProcessStrategy(ProcessStrategyInterface):
    def create_ordering(self, list_tickets: List[SupportTicket]) -> List[SupportTicket]:
        return list_tickets.copy()


class FILOProcessStrategy(ProcessStrategyInterface):
    def create_ordering(self, list_tickets: List[SupportTicket]) -> List[SupportTicket]:
        return list_tickets.copy().reverse()


class RandomProcessStrategy(ProcessStrategyInterface):
    def create_ordering(self, list_tickets: List[SupportTicket]) -> List[SupportTicket]:
        _list_tickets = list_tickets.copy()
        random.shuffle(_list_tickets)
        return _list_tickets

class BlackHoleProcessStrategy(ProcessStrategyInterface):
    def create_ordering(self, list_tickets: List[SupportTicket]) -> List[SupportTicket]:
        _list_tickets = list_tickets.copy()
        _list_tickets.pop(random.randint(0, len(_list_tickets) - 1))

        return _list_tickets

class CustomerSupport:
    def __init__(self, processing_strategy: ProcessStrategyInterface):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        ordered_tickets = self.processing_strategy.create_ordering(self.tickets)
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ordered_tickets:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")

# create the application
app = CustomerSupport(BlackHoleProcessStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
