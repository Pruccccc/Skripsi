-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Agu 2026 pada 08.46
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `deteksi_tomat_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `hasil_deteksi`
--

CREATE TABLE `hasil_deteksi` (
  `id` int(11) NOT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `label` varchar(100) DEFAULT NULL,
  `confidence` float DEFAULT NULL,
  `iou` float DEFAULT NULL,
  `precision_score` float DEFAULT NULL,
  `recall_score` float DEFAULT NULL,
  `map50` float DEFAULT NULL,
  `map5095` float DEFAULT NULL,
  `gejala` text DEFAULT NULL,
  `waktu` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `hasil_deteksi`
--

INSERT INTO `hasil_deteksi` (`id`, `gambar`, `label`, `confidence`, `iou`, `precision_score`, `recall_score`, `map50`, `map5095`, `gejala`, `waktu`) VALUES
(4, '20260706_161910.jpg', 'serangan_hama', 92.45, 96.06, 100, 92.15, 96.5, 93.7, 'Gejala berupa kerusakan permukaan akibat gigitan, lubang, bekas serangan, atau kerusakan jaringan oleh organisme pengganggu.', '2026-07-06 09:19:10'),
(5, '20260706_162525.jpg', 'bacterial_spot_fruit', 95.31, 97.81, 96.18, 96.88, 99.32, 98.37, 'Gejala berupa bercak kecil berwarna gelap pada permukaan buah tomat. Bercak dapat tampak kasar dan menyebar pada kulit buah.', '2026-07-06 09:25:25'),
(6, '20260706_163238.jpg', 'bacterial_spot_fruit', 52.2, 97.81, 96.18, 96.88, 99.32, 98.37, 'Gejala berupa bercak kecil berwarna gelap pada permukaan buah tomat. Bercak dapat tampak kasar dan menyebar pada kulit buah.', '2026-07-06 09:32:38'),
(7, '20260707_050652.jpg', 'serangan_hama', 92.95, 96.06, 100, 92.15, 96.5, 93.7, 'Gejala berupa kerusakan permukaan akibat gigitan, lubang, bekas serangan, atau kerusakan jaringan oleh organisme pengganggu.', '2026-07-06 22:06:52'),
(8, '20260708_091635.jpg', 'blossom_end_rot', 78.4, 98.36, 99.44, 100, 99.5, 98.9, 'Gejala berupa area busuk berwarna coklat hingga hitam pada bagian ujung bawah buah tomat.', '2026-07-08 02:16:35'),
(9, '20260708_092101.jpg', 'serangan_hama', 93.31, 96.06, 100, 92.15, 96.5, 93.7, 'Gejala berupa kerusakan permukaan akibat gigitan, lubang, bekas serangan, atau kerusakan jaringan oleh organisme pengganggu.', '2026-07-08 02:21:01'),
(10, '20260804_212531.jpg', 'bacterial_spot_fruit', 92.94, 97.81, 96.18, 96.88, 99.32, 98.37, 'Gejala berupa bercak kecil berwarna gelap pada permukaan buah tomat. Bercak dapat tampak kasar dan menyebar pada kulit buah.', '2026-08-04 14:25:31');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `hasil_deteksi`
--
ALTER TABLE `hasil_deteksi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `hasil_deteksi`
--
ALTER TABLE `hasil_deteksi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
