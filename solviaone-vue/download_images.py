import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = [
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuD2f-ZhutWnn6eGBx_LHka9U23Zq96iDnJz_GC1VxLW4-vo9Yezc0bwanEKEgRlFdBNbSY6KtbBW6EDa52JNaCM13-PJ3ChcoVoaQp7QO3r1idKqGE776CBMfIWzpAalHLKevCIM-RIuZKh5CaA1z1Jg0goPc22f2qyDpwOsoid4Knok0PbVpzMH_nVN8qk2fZ_psy0nFKYVnziIa8-ElM0nUTpEgylo5I-3rg_xoyVFUjbKjFDeTWdpWnACRBfJL9BO-tON6e5nl0",
        "filename": "hero-team.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuAVjMlsPTtYKTN1a2Yyyq8sgBA_69PBTKYxpGxpZaY-0b17tTGLnhOx5_EkVvH_sxeDmO9D-8fkwvmzxSlV-PCy-DzmsfgjM4aueTDuhRW0shd-Ccf5ndtAQiM1cG6wRSVZKqQwpUoL6Xceb3acOKhN6tYfB2yaftgwxW56tdiF6CHDaezvx9msXjE1E0gOM907J5B1czGyBbNoszCVyPgv0_0VvIqWz4U_jrWh3nl_k2Q8zny1R7A6xUWrVWRVrUMFpILelfh7qhQ",
        "filename": "modern-office.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuC4UlN7z-eLBiqcoisQrxkErZIrtzKZTk7qVFwUU2f7QqOrDLM-uOm-0PkyQVASRgnei2RMAVwVrIp9_xnrpvI2YpaT441bwNuF_Pl70L1CsdP8RNNxg5HHejypEDkR9JZg1UdydBLyWS7wHEkv-RO5txyqHgkppySQa3Q7bbXyGzNjTx63FlXP297t3Rfs7Y9y0pMf_Gzmzu-PS4SvmGanIiNR_njafWA-7GNKMkOeOH8LhYe0yVPsdArTKov5AlFGdDzDQ94DdNw",
        "filename": "server-room.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBKDbsamgASVP4CKTD_ZSWMJbaoH9gvVZgKlzi3Jr1ofyP3JwKMKeOTbIMoz_Jt7qUwo6U5r7fCMLhI-JyqwfR9kInfBVKk0EdR_0ZKWprAuMpxZXsOt28iqVFG8aMAMlBOgpOZrCetvnuuZr33p-u4m_njGyv5WK1cpu_VcPhlP5zmtNnivIJFAEYFqKlx0sI0wWEEyWwL0hnHBuWdbH2ezqbEMsdiOJ5XxZdGrHWsJcETRfVIEX8jVwCGFKc5pN3PNv7QqpvqI80",
        "filename": "office-meeting.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDX_gZ5AQNjHYIZkAIbotIxcab_svADXlr8eGs_eUm4KKZ_RLWSW_-GeLlUBtASuIkkWO8UOStvUdQvPmaN_vCBPj475IUSiZtvXBJYP3dEWbc9NhgfB_ai5Um1V4Pxx7RwjevThpIt_gMuqmWsHo-Nqs95u3lKv9qSlZCnHmxTxMmJPUscQ6AaF7s6tA4p3fmi946oeVKDIl0GVnLF6Xgt9rp_iDF_3jCXDNtclkWqklbRLuFPj5K8xmkJiequ-F1XOgiZ17ZL2-Q",
        "filename": "tech-infrastructure.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuA4Lb3cjbw5lCu1hDjLKi6NpRGdjuPdgC2jM-6eHeiCi9QW1TIQz1wvnLT80K6IZOMUVQ6-0hR5m8LWlg0ATRf6WgdOTfU9u9biL6nIQd68S3L6BCaz9zmlNWizamuZIA24Cpaw8k0sxxwGu_ud2WKOnxgLDEi2r36eONk051ri5x2xUsDGscVuevmXCZO41Og-jJGiDhB68paz3Kadil9kUYnPFuOvtxacfMy1-ZPLYxbSyAg6udxrermbhGBJGy5OJIf5GFrzMWo",
        "filename": "case-office-workflow.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDQphZSTvD0YEMzYcMbNJKj7bu6Vmoj-oZgkBCODFIrjeFvp5VSD2NSj12iR_8ek9vg17q7casUQo-h5qd71wx91gwwUtXc43HlQJKZla5LUkaRTqEatzl1k5SpUweDeYW2hGKY7uBa5H0R7J3_OycmElpz2PHDg00l_yjl0QZlpZtFRejmhZZD5MT-zUDvSIyYVv0AYfIBWlJqUUOHRhOVIWSCqTw1fN14KKWMUt9W53kp-Ew9qznWJG28WOHM9uFwc51B1ZTB72Q",
        "filename": "case-retail-shop.jpg"
    },
    {
        "url": "https://lh3.googleusercontent.com/aida-public/AB6AXuCIYY3luCYzQQI31NNNILzzhcR9zlXnyHC1wm2GvhQLat4SvBetThUpYI3EdVeQM8_cez6uduiB7ZsIV6VAUGhNf_jNBkXs8Lktrf3FC-TD_WHQGzWjQKWUOyZYWDcTJkjDcFzA07r5D9K_bYKQOKganr75SYiaM00IQV_Y-a1HWzFsvuulu-elZ4sCLwrUYP_Tzn16vKez8oKDQ9K2f4nelU4p5uYClX0dhNSzcxfGQhHOTPmkXhYYkodxmCa6ZwthUcxgRXlrtKo",
        "filename": "case-dashboard.jpg"
    }
]

output_dir = "public/images"
os.makedirs(output_dir, exist_ok=True)

for img in images:
    output_path = os.path.join(output_dir, img["filename"])
    print(f"Downloading {img['filename']}...")
    try:
        urllib.request.urlretrieve(img["url"], output_path)
        print(f"  Saved to {output_path}")
    except Exception as e:
        print(f"  Error: {e}")

print("\nAll downloads completed!")
