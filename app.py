import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def format_vnd(value):
    return f"{int(value):,}"

def parse_vnd(text, default=0.0):
    cleaned = str(text).replace(",", "").replace(" ", "").strip()
    if cleaned == "":
        return float(default)
    try:
        return float(cleaned)
    except ValueError:
        return float(default)

st.set_page_config(page_title="Lan Chi Finance", page_icon="✨", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 18% 16%, rgba(255, 214, 235, 0.20), transparent 18%),
        radial-gradient(circle at 82% 14%, rgba(181, 196, 255, 0.24), transparent 24%),
        radial-gradient(circle at 70% 55%, rgba(170, 145, 255, 0.20), transparent 28%),
        radial-gradient(circle at 90% 38%, rgba(116, 162, 255, 0.22), transparent 18%),
        linear-gradient(135deg, #07111f 0%, #0b1630 30%, #111d45 55%, #1c1f57 78%, #121634 100%);
    color: #f7f3ff;
}

.block-container {
    max-width: 1220px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 34px 30px 34px;
    border-radius: 28px;
    background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05));
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 18px 60px rgba(10, 12, 35, 0.28);
    backdrop-filter: blur(10px);
    margin-bottom: 22px;
}

.hero::after {
    content: "";
    position: absolute;
    inset: auto -60px -80px auto;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(248,181,219,0.26), rgba(162,180,255,0.0) 68%);
    filter: blur(8px);
}

.brand {
    font-size: 14px;
    letter-spacing: 1.6px;
    color: #d9cfff;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-title {
    font-size: 48px;
    line-height: 1.05;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
}

.hero-sub {
    font-size: 18px;
    color: #d6ddff;
    max-width: 720px;
    line-height: 1.75;
}

.soft-chip-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 18px;
}

.soft-chip {
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    color: #fff5fb;
    background: rgba(255, 214, 235, 0.12);
    border: 1px solid rgba(255,255,255,0.10);
}

.card {
    padding: 24px;
    border-radius: 24px;
    background: linear-gradient(180deg, rgba(255,255,255,0.095), rgba(255,255,255,0.045));
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 12px 40px rgba(12, 14, 36, 0.20);
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #fff4fb;
    margin-bottom: 14px;
}

.section-note {
    font-size: 15px;
    line-height: 1.7;
    color: #dbe1ff;
}

.report-box-harvest {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.86));
    padding: 26px;
    border-radius: 24px;
    border-left: 10px solid #c3a1ff;
    box-shadow: 0 16px 40px rgba(195, 161, 255, 0.10);
}

.metric-shell {
    padding: 16px 18px;
    border-radius: 18px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-label {
    color: #ecdfff;
    font-size: 13px;
    margin-bottom: 4px;
}

.metric-value {
    color: #ffffff;
    font-weight: 800;
    font-size: 28px;
}

.small-soft {
    color: #dce2ff;
    font-size: 14px;
    line-height: 1.7;
}

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.10) !important;
    color: #0f1733 !important;
    -webkit-text-fill-color: #0f1733 !important;
    caret-color: #0f1733 !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    font-weight: 700 !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #6f7798 !important;
    -webkit-text-fill-color: #6f7798 !important;
}

label, .stMarkdown, p {
    color: #f4efff !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #f3b6db, #c3a1ff);
    color: #18203d;
    border: none;
    padding: 0.8rem 1.25rem;
    border-radius: 16px;
    font-weight: 800;
    box-shadow: 0 12px 28px rgba(243, 182, 219, 0.26);
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="brand">Lan Chi Finance</div>
    <div class="hero-title">Công cụ tài chính gọn, dễ nhìn, dễ dùng</div>
    <div class="hero-sub">
        Bảng tính giúp khách hàng nhìn nhanh vốn, lãi lỗ và điểm hòa vốn để chốt quyết định dễ hơn.
    </div>
    <div class="soft-chip-row">
        <div class="soft-chip">Theo dõi vốn</div>
        <div class="soft-chip">Nhìn nhanh hòa vốn</div>
        <div class="soft-chip">So sánh lãi lỗ trực quan</div>
    </div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.05, 0.95])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Bảng tính thu hồi vốn</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-note">Nhập nhanh vài con số để xem cần bán bao nhiêu, tài sản còn lại là bao nhiêu và hiện tại đã gần hòa vốn hay chưa.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        ticker_ph = st.text_input("Mã cổ phiếu", value="VND").upper()
        tong_von_goc_text = st.text_input("Tổng vốn đầu tư ban đầu (VNĐ)", value=format_vnd(100000000), placeholder="100,000,000")
        tong_von_goc = parse_vnd(tong_von_goc_text, 100000000)
    with col2:
        so_luong_co_text = st.text_input("Số lượng đang nắm giữ", value=format_vnd(5000), placeholder="5,000")
        so_luong_co = parse_vnd(so_luong_co_text, 5000)
        gia_thi_truong_text = st.text_input("Giá thị trường hiện tại (VNĐ)", value=format_vnd(35000), placeholder="35,000")
        gia_thi_truong = parse_vnd(gia_thi_truong_text, 35000)

    st.markdown('</div>', unsafe_allow_html=True)

phi_moi_gioi = 0.0015
thue_ban = 0.001
tong_phi_thue = phi_moi_gioi + thue_ban

so_luong_ban = tong_von_goc / (gia_thi_truong * (1 - tong_phi_thue)) if gia_thi_truong > 0 else 0
current_gross_value = so_luong_co * gia_thi_truong
current_net_value = current_gross_value * (1 - tong_phi_thue)
profit_loss = current_net_value - tong_von_goc
gia_hoa_von_thuc = ((tong_von_goc / so_luong_co) / (1 - tong_phi_thue)) if so_luong_co > 0 else 0
so_luong_con_lai = max(so_luong_co - so_luong_ban, 0)
gia_tri_0_dong = so_luong_con_lai * gia_thi_truong

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Nhìn nhanh</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-soft">Nếu giá hiện tại chưa đủ để rút gốc sau phí, bảng sẽ hiện ngay vùng còn thiếu. Nếu đủ rồi, khách hàng nhìn luôn được phần tài sản còn lại.</div>', unsafe_allow_html=True)

    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f'''<div class="metric-shell"><div class="metric-label">Giá hòa vốn thực nhận</div><div class="metric-value">{gia_hoa_von_thuc:,.0f}đ</div></div>''', unsafe_allow_html=True)
    with m2:
        st.markdown(f'''<div class="metric-shell"><div class="metric-label">Giá hiện tại</div><div class="metric-value">{gia_thi_truong:,.0f}đ</div></div>''', unsafe_allow_html=True)

    st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
    near_text = "Đã hòa vốn" if profit_loss >= 0 else "Chưa hòa vốn"
    color_note = "#ffd7ea" if profit_loss >= 0 else "#ffe2e2"
    st.markdown(f'''<div class="metric-shell"><div class="metric-label">Trạng thái hiện tại</div><div class="metric-value" style="font-size:24px;color:{color_note};">{near_text}</div></div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)

if st.button("Tính điểm thu hồi vốn"):
    if so_luong_ban > so_luong_co:
        st.error(f"Hiện tại tài sản chưa đủ để rút gốc. {ticker_ph} cần đạt tối thiểu {gia_hoa_von_thuc:,.0f}đ để hòa vốn thực nhận sau phí.")
    else:
        st.markdown(f"""
        <div class="report-box-harvest">
        <table style="width:100%; border-collapse: collapse; font-family: Arial, sans-serif;">
            <tr style="border-bottom: 1px solid #efe7fb;">
                <td style="padding: 15px; color: #49326b;"><b>Số lượng cần bán để rút gốc</b></td>
                <td style="text-align: right; font-weight: bold; color: #a067d6;">{int(so_luong_ban + 1):,.0f} CP</td>
            </tr>
            <tr style="border-bottom: 1px solid #efe7fb;">
                <td style="padding: 15px; color: #49326b;"><b>Chi phí giao dịch (0.25%)</b></td>
                <td style="text-align: right; color: #a067d6;">~ {(tong_von_goc * tong_phi_thue):,.0f} đ</td>
            </tr>
            <tr style="background-color: #fff8fd; border-bottom: 1px solid #efe7fb;">
                <td style="padding: 15px; color: #49326b;"><b>Tài sản còn lại sau khi rút gốc</b></td>
                <td style="text-align: right; color: #9e7af3; font-size: 1.25em;"><b>{int(so_luong_con_lai):,.0f} CP</b></td>
            </tr>
            <tr>
                <td style="padding: 15px; color: #6a5ac9;">Giá trị phần còn lại theo giá hiện tại</td>
                <td style="text-align: right; color: #9e7af3;">{gia_tri_0_dong:,.0f} đ</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)
        st.success(f"Bán khoảng {int(so_luong_ban + 1):,.0f} CP là thu hồi đủ vốn gốc. Phần còn lại là tài sản giữ tiếp để chờ vùng lời đẹp hơn.")

st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Dashboard nhìn nhanh vốn và lãi lỗ</div>', unsafe_allow_html=True)
st.markdown('<div class="small-soft">Biểu đồ này để khách hàng nhìn sơ qua là biết tổng tài sản hiện tại đang dưới vốn, sát hòa vốn hay đã vượt lên vùng lời.</div>', unsafe_allow_html=True)

chart_df = pd.DataFrame({
    "Hạng mục": ["Vốn gốc", "Giá trị hiện tại sau phí", "Lãi / Lỗ"],
    "Giá trị": [tong_von_goc, current_net_value, abs(profit_loss)]
})

fig, ax = plt.subplots(figsize=(8, 4.8))
bars = ax.bar(
    chart_df["Hạng mục"],
    chart_df["Giá trị"],
    color=["#ffd6e8", "#f8b7da", "#e8d8ff"]
)
ax.set_facecolor((1, 1, 1, 0.02))
fig.patch.set_alpha(0)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.spines['bottom'].set_color('#d8d9ff')
ax.tick_params(axis='x', colors='#f7efff', labelsize=11)
ax.tick_params(axis='y', colors='#dfe3ff', labelsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.18)
ax.set_ylabel('VNĐ', color='#f3ecff')
ax.set_title('So sánh nhanh', color='#fff5fb', fontsize=14, pad=12)

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:,.0f}",
        ha='center', va='bottom', color='#fff7fb', fontsize=10
    )

st.pyplot(fig, use_container_width=True)

if profit_loss >= 0:
    st.info(f"Hiện giá trị sau phí đang cao hơn vốn gốc khoảng {profit_loss:,.0f} đ. Khách hàng nhìn vào là biết đã qua vùng hòa vốn.")
else:
    st.info(f"Hiện còn cách hòa vốn khoảng {abs(profit_loss):,.0f} đ. Nhìn biểu đồ là thấy đang tiến gần vùng cân bằng hay chưa.")

st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.caption("© 2026 Lan Chi Finance | Phí mặc định: môi giới 0.15% + thuế bán 0.1%")
st.caption("Mẹo nhập liệu: có thể gõ 100000000 hoặc 100,000,000, hệ thống đều hiểu.")