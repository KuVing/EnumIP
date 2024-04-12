#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ipaddress

def main():
    while True:
        ip_range_input = input("请输入IP地址范围:")

        start_ip, end_ip = ip_range_input.split("-")
        start_last_octet = int(start_ip.split(".")[-1])
        end_last_octet = int(end_ip)
        base_ip = ".".join(start_ip.split(".")[:-1])

        with open("ip.txt", "a") as ip_file:
            for i in range(start_last_octet, end_last_octet + 1):
                ip = f"{base_ip}.{i}"
                ip_file.write(ip + "\n")
                print(ip)

        user_input = input("是否继续？（输入y继续，输入其他任意键退出）：")
        if user_input.lower() != "y":
            break


if __name__ == "__main__":
    main()