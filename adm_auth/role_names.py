from .constants import (
    ACCOUNT_MANAGER_ROLE,
    CUSTOM_ROLE,
    STAFF_ROLE,
    CLINIC_SUPER_ROLE,
    CLINIC_ROLE,
    LABORATORY_ROLE,
    HISTOPATHOLOGY_ROLE,
    MOLECULAR_GENETICS_ROLE,
    HM_LOCATOR_AIR_MONITOR_ROLE,

)
from .group_names import (
    ACCOUNT_MANAGER,
    ADMINISTRATION,
    EVERYONE,
    CLINIC_SUPER,
    CLINIC,
    LABORATORY,
    HISTOPATHOLOGY,
    MOLECULAR_GENETICS,
    HM_LOCATOR_AIR_MONITOR,
)

role_names = {
    ACCOUNT_MANAGER_ROLE: "Account Manager",
    CLINIC_SUPER_ROLE: "Clinic Super",
    CLINIC_ROLE: "Clinic",
    CUSTOM_ROLE: "Custom ...",
    STAFF_ROLE: "Staff",
    LABORATORY_ROLE: "Laboratory",
    HISTOPATHOLOGY_ROLE: "Histopathology",
    MOLECULAR_GENETICS_ROLE: "Molecular genetics",
    HM_LOCATOR_AIR_MONITOR_ROLE: "Home Locator Air Monitoring"
}

required_role_names = {STAFF_ROLE: "Staff"}

groups_by_role_name = {
    ACCOUNT_MANAGER_ROLE: [ACCOUNT_MANAGER, ADMINISTRATION, EVERYONE],
    CLINIC_SUPER_ROLE: [CLINIC, CLINIC_SUPER, EVERYONE],
    CLINIC_ROLE: [CLINIC, EVERYONE],
    STAFF_ROLE: [EVERYONE],
    LABORATORY_ROLE: [LABORATORY, EVERYONE],
    HISTOPATHOLOGY_ROLE: [HISTOPATHOLOGY],
    MOLECULAR_GENETICS_ROLE: [MOLECULAR_GENETICS],
    HM_LOCATOR_AIR_MONITOR_ROLE: [HM_LOCATOR_AIR_MONITOR],
    CUSTOM_ROLE: [],
}
