import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
isp_data = pd.read_csv("dns_isp.csv")
google_data = pd.read_csv("dns_google_8.8.8.8.csv")
cloudflare_data = pd.read_csv("dns_cloudflare_1.1.1.1.csv")

# Function to analyze response times
def analyze_response_times(data, name):
    min_time = data['Time'].min()
    max_time = data['Time'].max()
    avg_time = data['Time'].mean()
    return min_time, max_time, avg_time

# Get statistics for each DNS
isp_stats = analyze_response_times(isp_data, "ISP")
google_stats = analyze_response_times(google_data, "Google (8.8.8.8)")
cloudflare_stats = analyze_response_times(cloudflare_data, "Cloudflare (1.1.1.1)")

dns_stats = {
    "ISP": isp_stats,
    "Google (8.8.8.8)": google_stats,
    "Cloudflare (1.1.1.1)": cloudflare_stats
}

# Determine the fastest DNS (lowest average response time)
fastest_dns = min(dns_stats, key=lambda x: dns_stats[x][2])

# Generate bar chart for comparison
labels = list(dns_stats.keys())
min_times = [stats[0] for stats in dns_stats.values()]
max_times = [stats[1] for stats in dns_stats.values()]
avg_times = [stats[2] for stats in dns_stats.values()]

x = range(len(labels))
plt.figure(figsize=(10, 6))
plt.bar(x, avg_times, color=['blue', 'red', 'green'])
plt.xticks(x, labels)
plt.ylabel("Response Time (ms)")
plt.title("Average DNS Response Time Comparison")
plt.savefig("dns_comparison_bar.png")
plt.show()

# Save results in a report
with open("dns_analysis_report.txt", "w") as report:
    report.write("DNS Response Time Analysis\n")
    report.write("===========================\n\n")
    for dns, stats in dns_stats.items():
        report.write(f"{dns} DNS Statistics:\n")
        report.write(f"Minimum Response Time: {stats[0]} ms\n")
        report.write(f"Maximum Response Time: {stats[1]} ms\n")
        report.write(f"Average Response Time: {stats[2]} ms\n\n")
    report.write(f"\nFastest DNS Server: {fastest_dns}\n")
    report.write("Check 'dns_comparison_bar.png' for a visual comparison.\n")

print(f"\n✅ Fastest DNS Server: {fastest_dns}")
print("✅ Analysis Complete! Check 'dns_analysis_report.txt' for details.")
print("✅ Bar graph saved as 'dns_comparison_bar.png'.")
