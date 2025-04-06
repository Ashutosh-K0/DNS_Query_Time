import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV files
isp_data = pd.read_csv("dns_isp.csv")
google_data = pd.read_csv("dns_google_8.8.8.8.csv")
cloudflare_data = pd.read_csv("dns_cloudflare_1.1.1.1.csv")

# Function to analyze response times
def analyze_response_times(data, name):
    min_time = data['Time'].min()
    max_time = data['Time'].max()
    avg_time = data['Time'].mean()

    print(f"\n{name} DNS Statistics:")
    print(f"Minimum Response Time: {min_time:.3f} ms")
    print(f"Maximum Response Time: {max_time:.3f} ms")
    print(f"Average Response Time: {avg_time:.3f} ms\n")

    return min_time, max_time, avg_time, data['Time']

# Get statistics for each DNS
isp_stats = analyze_response_times(isp_data, "ISP")
google_stats = analyze_response_times(google_data, "Google (8.8.8.8)")
cloudflare_stats = analyze_response_times(cloudflare_data, "Cloudflare (1.1.1.1)")

# --- PLOT 1: Line Graph for Response Time Trend ---
plt.figure(figsize=(10, 5))
plt.plot(isp_data['Time'], label="ISP DNS", marker="o", linestyle="dashed")
plt.plot(google_data['Time'], label="Google DNS (8.8.8.8)", marker="s", linestyle="dotted")
plt.plot(cloudflare_data['Time'], label="Cloudflare DNS (1.1.1.1)", marker="^", linestyle="-")

plt.xlabel("Query Number")
plt.ylabel("Response Time (ms)")
plt.title("DNS Query Response Times Over Queries")
plt.legend()
plt.grid()
plt.savefig("dns_response_trend.png")  # Save graph as an image
plt.show()

# --- PLOT 2: Bar Graph for Min, Max, and Average Response Times ---
labels = ["ISP", "Google (8.8.8.8)", "Cloudflare (1.1.1.1)"]
min_times = [isp_stats[0], google_stats[0], cloudflare_stats[0]]
max_times = [isp_stats[1], google_stats[1], cloudflare_stats[1]]
avg_times = [isp_stats[2], google_stats[2], cloudflare_stats[2]]

x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, min_times, width, label="Minimum Time", color='green')
ax.bar(x, avg_times, width, label="Average Time", color='blue')
ax.bar(x + width, max_times, width, label="Maximum Time", color='red')

ax.set_xlabel("DNS Server")
ax.set_ylabel("Response Time (ms)")
ax.set_title("Comparison of Min, Max, and Average Response Times")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.grid(axis='y')
plt.savefig("dns_response_comparison.png")
plt.show()

# --- PLOT 3: Box Plot for Response Time Distribution ---
plt.figure(figsize=(10, 6))
plt.boxplot([isp_stats[3], google_stats[3], cloudflare_stats[3]], labels=labels)

plt.xlabel("DNS Server")
plt.ylabel("Response Time (ms)")
plt.title("Distribution of DNS Query Response Times")
plt.grid()
plt.savefig("dns_response_distribution.png")
plt.show()

# Save results in a text report
with open("dns_analysis_report.txt", "w") as report:
    report.write("DNS Response Time Analysis\n")
    report.write("===========================\n\n")
    
    report.write("ISP DNS Statistics:\n")
    report.write(f"Minimum Response Time: {isp_stats[0]:.3f} ms\n")
    report.write(f"Maximum Response Time: {isp_stats[1]:.3f} ms\n")
    report.write(f"Average Response Time: {isp_stats[2]:.3f} ms\n\n")

    report.write("Google DNS (8.8.8.8) Statistics:\n")
    report.write(f"Minimum Response Time: {google_stats[0]:.3f} ms\n")
    report.write(f"Maximum Response Time: {google_stats[1]:.3f} ms\n")
    report.write(f"Average Response Time: {google_stats[2]:.3f} ms\n\n")

    report.write("Cloudflare DNS (1.1.1.1) Statistics:\n")
    report.write(f"Minimum Response Time: {cloudflare_stats[0]:.3f} ms\n")
    report.write(f"Maximum Response Time: {cloudflare_stats[1]:.3f} ms\n")
    report.write(f"Average Response Time: {cloudflare_stats[2]:.3f} ms\n\n")

    report.write("Conclusion:\n")
    fastest_dns = min(isp_stats[2], google_stats[2], cloudflare_stats[2])
    
    if fastest_dns == isp_stats[2]:
        report.write("The ISP DNS had the fastest average response time.\n")
    elif fastest_dns == google_stats[2]:
        report.write("Google DNS (8.8.8.8) had the fastest average response time.\n")
    else:
        report.write("Cloudflare DNS (1.1.1.1) had the fastest average response time.\n")

    # Analyzing lowest maximum response time
    lowest_max_dns = min(isp_stats[1], google_stats[1], cloudflare_stats[1])
    if lowest_max_dns == isp_stats[1]:
        report.write("The ISP DNS had the lowest maximum response time, indicating stable performance.\n")
    elif lowest_max_dns == google_stats[1]:
        report.write("Google DNS (8.8.8.8) had the lowest maximum response time, indicating stable performance.\n")
    else:
        report.write("Cloudflare DNS (1.1.1.1) had the lowest maximum response time, indicating stable performance.\n")

    report.write("\nCheck the graphs for a visual representation:\n")
    report.write(" - dns_response_trend.png (Line Graph of Query Times)\n")
    report.write(" - dns_response_comparison.png (Bar Graph of Min, Max, Avg)\n")
    report.write(" - dns_response_distribution.png (Box Plot of Distribution)\n")

print("\n✅ Analysis Complete! Check 'dns_analysis_report.txt' for details.")
print("✅ Graphs saved as 'dns_response_trend.png', 'dns_response_comparison.png', and 'dns_response_distribution.png'.")
