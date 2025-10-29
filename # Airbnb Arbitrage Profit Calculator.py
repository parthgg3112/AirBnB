# Airbnb Arbitrage Profit Calculator

def airbnb_arbitrage(
    monthly_rent,
    nightly_rate,
    occupancy_nights,
    setup_cost,
    cleaning_utilities=20000,
    platform_fee_percent=3
):
    # Revenue from Airbnb
    gross_revenue = nightly_rate * occupancy_nights
    
    # Platform fee
    platform_fee = gross_revenue * platform_fee_percent / 100
    
    # Total monthly expenses
    total_expenses = monthly_rent + cleaning_utilities + platform_fee
    
    # Net profit
    net_profit = gross_revenue - total_expenses
    
    # Annual profit
    annual_profit = net_profit * 12
    
    # ROI and payback period
    if setup_cost > 0:
        roi_percent = (annual_profit / setup_cost) * 100
        payback_months = setup_cost / net_profit if net_profit > 0 else None
    else:
        roi_percent = 0
        payback_months = None
    
    print("\n📊 Airbnb Arbitrage Simulation")
    print("-" * 35)
    print(f"Nightly Rate: ₹{nightly_rate}")
    print(f"Occupancy: {occupancy_nights} nights/month")
    print(f"Monthly Rent: ₹{monthly_rent}")
    print(f"Cleaning & Utilities: ₹{cleaning_utilities}")
    print(f"Platform Fee: ₹{platform_fee:,.0f}")
    print(f"\nGross Revenue: ₹{gross_revenue:,.0f}")
    print(f"Total Expenses: ₹{total_expenses:,.0f}")
    print(f"✅ Net Monthly Profit: ₹{net_profit:,.0f}")
    print(f"💰 Annual Profit: ₹{annual_profit:,.0f}")
    print(f"📈 ROI on Setup Cost: {roi_percent:.1f}%")
    if payback_months:
        print(f"⏳ Payback Period: {payback_months:.1f} months")
    print("-" * 35)

# Example: Goa 2BHK case
airbnb_arbitrage(
    monthly_rent=60000,
    nightly_rate=7000,
    occupancy_nights=20,
    setup_cost=400000,
    cleaning_utilities=20000,
    platform_fee_percent=3
)
