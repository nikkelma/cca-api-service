"""Important constants for the CCA Registry"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Province(models.TextChoices):
    """Enumeration of supported school provinces"""

    ALABAMA = "Alabama", _("Alabama")
    ALASKA = "Alaska", _("Alaska")
    ALBERTA = "Alberta", _("Alberta")
    AMERICAN_SAMOA = "American Samoa", _("American Samoa")
    ARIZONA = "Arizona", _("Arizona")
    ARKANSAS = "Arkansas", _("Arkansas")
    BRITISH_COLUMBIA = "British Columbia", _("British Columbia")
    CALIFORNIA = "California", _("California")
    COLORADO = "Colorado", _("Colorado")
    CONNECTICUT = "Connecticut", _("Connecticut")
    DELAWARE = "Delaware", _("Delaware")
    DISTRICT_OF_COLUMBIA = "District of Columbia", _("District of Columbia")
    FEDERATED_STATES_OF_MICRONESIA = (
        "Federated States of Micronesia",
        _("Federated States of Micronesia"),
    )
    FLORIDA = "Florida", _("Florida")
    GEORGIA = "Georgia", _("Georgia")
    GUAM = "Guam", _("Guam")
    HAWAII = "Hawaii", _("Hawaii")
    IDAHO = "Idaho", _("Idaho")
    ILLINOIS = "Illinois", _("Illinois")
    INDIANA = "Indiana", _("Indiana")
    IOWA = "Iowa", _("Iowa")
    KANSAS = "Kansas", _("Kansas")
    KENTUCKY = "Kentucky", _("Kentucky")
    LOUISIANA = "Louisiana", _("Louisiana")
    MAINE = "Maine", _("Maine")
    MANITOBA = "Manitoba", _("Manitoba")
    MARSHALL_ISLANDS = "Marshall Islands", _("Marshall Islands")
    MARYLAND = "Maryland", _("Maryland")
    MASSACHUSETTS = "Massachusetts", _("Massachusetts")
    MICHIGAN = "Michigan", _("Michigan")
    MINNESOTA = "Minnesota", _("Minnesota")
    MISSISSIPPI = "Mississippi", _("Mississippi")
    MISSOURI = "Missouri", _("Missouri")
    MONTANA = "Montana", _("Montana")
    NEBRASKA = "Nebraska", _("Nebraska")
    NEVADA = "Nevada", _("Nevada")
    NEW_BRUNSWICK = "New Brunswick", _("New Brunswick")
    NEW_HAMPSHIRE = "New Hampshire", _("New Hampshire")
    NEW_JERSEY = "New Jersey", _("New Jersey")
    NEW_MEXICO = "New Mexico", _("New Mexico")
    NEW_YORK = "New York", _("New York")
    NEWFOUNDLAND_AND_LABRADOR = (
        "Newfoundland and Labrador",
        _("Newfoundland and Labrador"),
    )
    NORTH_CAROLINA = "North Carolina", _("North Carolina")
    NORTH_DAKOTA = "North Dakota", _("North Dakota")
    NORTHERN_MARIANA_ISLANDS = (
        "Northern Mariana Islands",
        _("Northern Mariana Islands"),
    )
    NORTHWEST_TERRITORIES = "Northwest Territories", _("Northwest Territories")
    NOVA_SCOTIA = "Nova Scotia", _("Nova Scotia")
    NUNAVUT = "Nunavut", _("Nunavut")
    OHIO = "Ohio", _("Ohio")
    OKLAHOMA = "Oklahoma", _("Oklahoma")
    ONTARIO = "Ontario", _("Ontario")
    OREGON = "Oregon", _("Oregon")
    PALAU = "Palau", _("Palau")
    PENNSYLVANIA = "Pennsylvania", _("Pennsylvania")
    PRINCE_EDWARD_ISLAND = "Prince Edward Island", _("Prince Edward Island")
    PUERTO_RICO = "Puerto Rico", _("Puerto Rico")
    QUEBEC = "Quebec", _("Quebec")
    RHODE_ISLAND = "Rhode Island", _("Rhode Island")
    SASKATCHEWAN = "Saskatchewan", _("Saskatchewan")
    SOUTH_CAROLINA = "South Carolina", _("South Carolina")
    SOUTH_DAKOTA = "South Dakota", _("South Dakota")
    TENNESSEE = "Tennessee", _("Tennessee")
    TEXAS = "Texas", _("Texas")
    UTAH = "Utah", _("Utah")
    VERMONT = "Vermont", _("Vermont")
    VIRGIN_ISLANDS = "Virgin Islands", _("Virgin Islands")
    VIRGINIA = "Virginia", _("Virginia")
    WASHINGTON = "Washington", _("Washington")
    WEST_VIRGINIA = "West Virginia", _("West Virginia")
    WISCONSIN = "Wisconsin", _("Wisconsin")
    WYOMING = "Wyoming", _("Wyoming")
    YUKON = "Yukon", _("Yukon")


class Region(models.TextChoices):
    """Enumeration of supported school regions"""

    EAST = "EAST", _("East")
    WEST = "WEST", _("West")
