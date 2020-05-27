FROM opensuse/leap:15.1
COPY setup_environment_suse_leap_15.1.sh /suse_custom/install_deps.sh
RUN chmod u+x /suse_custom/install_deps.sh
RUN /suse_custom/install_deps.sh
