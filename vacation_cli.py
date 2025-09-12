#!/usr/bin/env python3
"""
Earth Vacation CLI - Interactive Command Line Interface
"""

import sys
from earth_vacation import EarthVacationPlanner


def print_header():
    """Print the application header."""
    print("🛸" + "=" * 48 + "🌍")
    print("     ALIEN TELEPATHY EARTH VACATION SYSTEM")
    print("🛸" + "=" * 48 + "🌍")


def print_menu():
    """Print the main menu options."""
    print("\nChoose an option:")
    print("1. View Earth vacation destinations")
    print("2. Book a vacation")
    print("3. View booking details")
    print("4. Send telepathic confirmation")
    print("5. Exit")


def view_destinations(planner):
    """Display all available destinations."""
    print("\n🌍 EARTH VACATION DESTINATIONS 🌍")
    print("-" * 40)
    
    destinations = planner.list_destinations()
    for i, dest in enumerate(destinations, 1):
        print(f"\n{i}. {dest['name']}")
        print(f"   ID: {dest['id']}")
        print(f"   Location: {dest['location']}")
        print(f"   Duration: {dest['duration_days']} Earth days")
        print(f"   Price: {dest['price_energy_units']} energy units")
        print(f"   Max Aliens: {dest['max_aliens']}")
        print(f"   Telepathy Level: {dest['telepathy_frequency']}")
        print(f"   Description: {dest['description']}")


def book_vacation(planner):
    """Handle vacation booking."""
    print("\n📝 BOOKING EARTH VACATION")
    print("-" * 30)
    
    alien_id = input("Enter your Alien ID: ").strip()
    if not alien_id:
        print("❌ Alien ID is required!")
        return
    
    print("\nAvailable destinations:")
    destinations = planner.list_destinations()
    for i, dest in enumerate(destinations, 1):
        print(f"{i}. {dest['name']} ({dest['id']})")
    
    try:
        choice = int(input("\nSelect destination (1-3): "))
        if choice < 1 or choice > len(destinations):
            print("❌ Invalid choice!")
            return
        
        destination_id = destinations[choice - 1]['id']
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    if not start_date:
        print("❌ Start date is required!")
        return
    
    booking = planner.book_vacation(alien_id, destination_id, start_date)
    
    if booking.get("status") == "error":
        print(f"❌ Booking failed: {booking['message']}")
    else:
        print(f"\n✅ Booking successful!")
        print(f"Booking ID: {booking['booking_id']}")
        print(f"Destination: {booking['destination']['name']}")
        print(f"Dates: {booking['start_date']} to {booking['end_date']}")


def view_booking(planner):
    """View booking details."""
    print("\n🔍 VIEW BOOKING DETAILS")
    print("-" * 25)
    
    booking_id = input("Enter Booking ID: ").strip()
    if not booking_id:
        print("❌ Booking ID is required!")
        return
    
    booking = planner.get_booking(booking_id)
    if not booking:
        print("❌ Booking not found!")
        return
    
    print(f"\n📋 Booking Details:")
    print(f"Booking ID: {booking['booking_id']}")
    print(f"Alien ID: {booking['alien_id']}")
    print(f"Destination: {booking['destination']['name']}")
    print(f"Location: {booking['destination']['location']}")
    print(f"Dates: {booking['start_date']} to {booking['end_date']}")
    print(f"Status: {booking['status']}")
    print(f"Telepathy Channel: {booking['telepathy_channel']}")


def send_confirmation(planner):
    """Send telepathic confirmation."""
    print("\n📡 SEND TELEPATHIC CONFIRMATION")
    print("-" * 35)
    
    booking_id = input("Enter Booking ID: ").strip()
    if not booking_id:
        print("❌ Booking ID is required!")
        return
    
    confirmation = planner.send_telepathic_confirmation(booking_id)
    print(confirmation)


def main():
    """Main CLI application."""
    planner = EarthVacationPlanner()
    
    print_header()
    print("Welcome to the Alien Telepathy Earth Vacation System!")
    print("Plan your perfect vacation to observe those curious Earthlings!")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                view_destinations(planner)
            elif choice == "2":
                book_vacation(planner)
            elif choice == "3":
                view_booking(planner)
            elif choice == "4":
                send_confirmation(planner)
            elif choice == "5":
                print("\n🛸 Safe travels through the cosmos! 🌌")
                break
            else:
                print("❌ Invalid choice! Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n🛸 Safe travels through the cosmos! 🌌")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()