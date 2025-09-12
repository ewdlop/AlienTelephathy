#!/usr/bin/env python3
"""
Demo script showing Earth Vacation functionality
"""

from earth_vacation import EarthVacationPlanner
import json


def demo_earth_vacation():
    """Comprehensive demo of the Earth vacation system."""
    print("🛸" + "=" * 60 + "🌍")
    print("            EARTH VACATION SYSTEM DEMO")
    print("🛸" + "=" * 60 + "🌍")
    
    # Initialize the planner
    planner = EarthVacationPlanner()
    
    print("\n1. 📋 AVAILABLE VACATION PACKAGES:")
    print("-" * 40)
    destinations = planner.list_destinations()
    for dest in destinations:
        print(f"• {dest['name']} ({dest['id']})")
        print(f"  📍 {dest['location']}")
        print(f"  ⏰ {dest['duration_days']} days | 💰 {dest['price_energy_units']} energy units")
        print(f"  📡 Telepathy: {dest['telepathy_frequency']}")
        if 'features' in dest:
            print(f"  ✨ Features: {', '.join(dest['features'][:2])}...")
        print()
    
    print("\n2. 🛸 BOOKING DEMONSTRATION:")
    print("-" * 40)
    
    # Demo multiple bookings
    demo_bookings = [
        ("ALIEN_ZETA_1", "earth_001", "2024-07-01"),
        ("ALIEN_ALPHA_7", "earth_004", "2024-08-15"),
        ("ALIEN_OMEGA_3", "earth_002", "2024-09-10")
    ]
    
    for alien_id, dest_id, start_date in demo_bookings:
        print(f"\n🎫 Booking for {alien_id}:")
        booking = planner.book_vacation(alien_id, dest_id, start_date)
        if booking.get("status") != "error":
            print(f"   ✅ Success! Booking ID: {booking['booking_id']}")
            print(f"   📅 {booking['start_date']} to {booking['end_date']}")
            print(f"   🏛️ {booking['destination']['name']}")
        else:
            print(f"   ❌ Failed: {booking['message']}")
    
    print("\n3. 📡 TELEPATHIC CONFIRMATIONS:")
    print("-" * 40)
    
    # Show confirmations for first booking
    if planner.bookings:
        booking_id = planner.bookings[0]['booking_id']
        confirmation = planner.send_telepathic_confirmation(booking_id)
        print(confirmation)
    
    print("\n4. 📊 BOOKING SUMMARY:")
    print("-" * 40)
    print(f"Total bookings processed: {len(planner.bookings)}")
    
    # Calculate total energy units
    total_energy = sum(booking['destination']['price_energy_units'] 
                      for booking in planner.bookings)
    print(f"Total energy units booked: {total_energy}")
    
    # Show telepathy protocols info
    if hasattr(planner, 'telepathy_protocols') and planner.telepathy_protocols:
        print(f"\nActive telepathy protocols: {len(planner.telepathy_protocols)}")
        for protocol, info in planner.telepathy_protocols.items():
            print(f"  • {protocol}: {info.get('description', 'N/A')}")
    
    print("\n🌌 Demo complete! The Earth vacation system is ready for alien tourism!")
    print("🛸" + "=" * 60 + "🌍")


if __name__ == "__main__":
    demo_earth_vacation()