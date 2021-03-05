# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

is_healthy = total_cholostrol < 200 and ldl < 100 and triglyceride < 150
has_high_colestoral = 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200
is_borderline_unhealthy = (
    200 < total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200
)


def start_tlc():
    print("Start TLC diet")
    print(
        "Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat."
    )
    print(
        "Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:"
    )
    print("oats, barley, and other whole grains.")
    print("fruits such as apples, pears, bananas, and oranges.")


if is_healthy:
    # good level
    print("*** Good level of cholestrol ***")
elif has_high_colestoral:
    # High cholestrol level
    print("*** High cholestrol level ***")
    print("start taking pills such as statins")
    start_tlc()
elif is_borderline_unhealthy:
    # TLC_diet
    print("*** Borderline to moderately elevated ***")
    start_tlc()
else:
    print("Error: unhandled case.")
