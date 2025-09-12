#!/usr/bin/env python3
"""
Earth Vacation Planning Module for Alien Telepathy Network

This module provides functionality for aliens to plan and book vacations to Earth.
Uses telepathic communication protocols for seamless booking experience.
"""

import json
import datetime
import os
from typing import Dict, List, Optional


class EarthVacationPlanner:
    """
    Main class for planning Earth vacations for alien tourists.
    """
    
    def __init__(self, config_file: str = "vacation_config.json"):
        self.config_file = config_file
        self.destinations = self._load_destinations()
        self.telepathy_protocols = self._load_telepathy_protocols()
        self.bookings = []
    
    def _load_destinations(self) -> List[Dict]:
        """Load available Earth vacation destinations from config file."""
        try:
            config_path = os.path.join(os.path.dirname(__file__), self.config_file)
            with open(config_path, 'r') as f:
                config = json.load(f)
            return config.get("earth_vacation_packages", [])
        except FileNotFoundError:
            # Fallback to hardcoded destinations if config file not found
            return [
                {
                    "id": "earth_001",
                    "name": "Human Settlement Observation Tour",
                    "location": "Various Earth Cities",
                    "description": "Observe human behavior patterns in their natural habitat",
                    "duration_days": 7,
                    "max_aliens": 50,
                    "telepathy_frequency": "low",
                    "price_energy_units": 1200
                }
            ]
    
    def _load_telepathy_protocols(self) -> Dict:
        """Load telepathy protocol configurations."""
        try:
            config_path = os.path.join(os.path.dirname(__file__), self.config_file)
            with open(config_path, 'r') as f:
                config = json.load(f)
            return config.get("telepathy_protocols", {})
        except FileNotFoundError:
            return {}
    
    def list_destinations(self) -> List[Dict]:
        """Return list of available Earth vacation destinations."""
        return self.destinations
    
    def book_vacation(self, alien_id: str, destination_id: str, start_date: str) -> Dict:
        """
        Book a vacation to Earth for an alien.
        
        Args:
            alien_id: Unique identifier for the alien
            destination_id: ID of the destination package
            start_date: Start date in YYYY-MM-DD format
            
        Returns:
            Booking confirmation dictionary
        """
        # Find destination
        destination = None
        for dest in self.destinations:
            if dest["id"] == destination_id:
                destination = dest
                break
        
        if not destination:
            return {"status": "error", "message": "Destination not found"}
        
        # Create booking
        booking = {
            "booking_id": f"EVB_{len(self.bookings) + 1:04d}",
            "alien_id": alien_id,
            "destination": destination,
            "start_date": start_date,
            "end_date": self._calculate_end_date(start_date, destination["duration_days"]),
            "status": "confirmed",
            "telepathy_channel": f"earth_vacation_{alien_id}",
            "booking_timestamp": datetime.datetime.now().isoformat()
        }
        
        self.bookings.append(booking)
        return booking
    
    def _calculate_end_date(self, start_date: str, duration_days: int) -> str:
        """Calculate end date based on start date and duration."""
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = start + datetime.timedelta(days=duration_days)
        return end.strftime("%Y-%m-%d")
    
    def get_booking(self, booking_id: str) -> Optional[Dict]:
        """Retrieve booking details by booking ID."""
        for booking in self.bookings:
            if booking["booking_id"] == booking_id:
                return booking
        return None
    
    def send_telepathic_confirmation(self, booking_id: str) -> str:
        """Send telepathic confirmation to alien about their booking."""
        booking = self.get_booking(booking_id)
        if not booking:
            return "Booking not found for telepathic transmission"
        
        message = f"""
        *TELEPATHIC TRANSMISSION INITIATED*
        
        Greetings {booking['alien_id']},
        
        Your Earth vacation has been confirmed!
        
        Destination: {booking['destination']['name']}
        Location: {booking['destination']['location']}
        Dates: {booking['start_date']} to {booking['end_date']}
        Telepathy Channel: {booking['telepathy_channel']}
        
        Remember: Use {booking['destination']['telepathy_frequency']} telepathy frequency
        to avoid overwhelming the local human population.
        
        Safe travels!
        
        *TRANSMISSION COMPLETE*
        """
        return message


def main():
    """Demo function showing Earth vacation planning in action."""
    print("🛸 Welcome to Earth Vacation Planning System 🌍")
    print("=" * 50)
    
    planner = EarthVacationPlanner()
    
    # Show available destinations
    print("\nAvailable Earth Vacation Packages:")
    destinations = planner.list_destinations()
    for dest in destinations:
        print(f"\n📍 {dest['name']}")
        print(f"   Location: {dest['location']}")
        print(f"   Duration: {dest['duration_days']} days")
        print(f"   Price: {dest['price_energy_units']} energy units")
        print(f"   Description: {dest['description']}")
    
    # Demo booking
    print("\n" + "=" * 50)
    print("Demo Booking:")
    booking = planner.book_vacation("ALIEN_X42", "earth_001", "2024-06-15")
    print(f"Booking created: {booking['booking_id']}")
    
    # Send confirmation
    confirmation = planner.send_telepathic_confirmation(booking['booking_id'])
    print(confirmation)


if __name__ == "__main__":
    main()