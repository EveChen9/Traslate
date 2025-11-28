#!/usr/bin/env python3
"""
Generate an interaction effect (moderation) line chart for a research paper.
This script creates a chart showing the relationship between AI Use and Moral Relativism
moderated by Task Ambiguity levels.

Output: figure_2.png (APA-style formatted chart)
"""

import matplotlib.pyplot as plt
import matplotlib


def create_interaction_chart():
    """Create and save the interaction effect chart."""
    
    # Set up the figure with white background
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
    ax.set_facecolor('white')
    
    # X-axis data points
    x_points = [0, 1]  # Low AI Use (-1 SD) and High AI Use (+1 SD)
    x_labels = ['Low AI Use (-1 SD)', 'High AI Use (+1 SD)']
    
    # Y-axis data points for each Task Ambiguity level
    # Low Task Ambiguity (-1 SD)
    y_low_ambiguity = [2.60, 3.84]
    
    # Mean Task Ambiguity
    y_mean_ambiguity = [2.42, 4.16]
    
    # High Task Ambiguity (+1 SD)
    y_high_ambiguity = [2.17, 4.41]
    
    # Use Times New Roman or a similar serif font
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Liberation Serif', 'serif']
    
    # Plot each line with specified styles
    # Low Task Ambiguity: Dotted line, Square markers, Dark Grey
    ax.plot(x_points, y_low_ambiguity, 
            linestyle=':', 
            marker='s', 
            color='dimgray',
            linewidth=2,
            markersize=10,
            label='Low Task Ambiguity')
    
    # Mean Task Ambiguity: Dashed line, Circle markers, Black
    ax.plot(x_points, y_mean_ambiguity, 
            linestyle='--', 
            marker='o', 
            color='black',
            linewidth=2,
            markersize=10,
            label='Mean Task Ambiguity')
    
    # High Task Ambiguity: Solid line, Triangle markers, Black
    ax.plot(x_points, y_high_ambiguity, 
            linestyle='-', 
            marker='^', 
            color='black',
            linewidth=2,
            markersize=10,
            label='High Task Ambiguity')
    
    # Set axis labels with serif font
    ax.set_xlabel('AI Use', fontsize=12, fontweight='normal', fontfamily='serif')
    ax.set_ylabel('Moral Relativism', fontsize=12, fontweight='normal', fontfamily='serif')
    
    # Set x-tick labels
    ax.set_xticks(x_points)
    ax.set_xticklabels(x_labels, fontsize=10, fontfamily='serif')
    
    # Format y-axis
    ax.tick_params(axis='y', labelsize=10)
    
    # Remove grid lines (APA style)
    ax.grid(False)
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Set spine colors to black for high contrast
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['left'].set_linewidth(1)
    
    # Add legend in upper left (clear spot)
    ax.legend(loc='upper left', 
              frameon=True, 
              framealpha=1,
              edgecolor='black',
              fontsize=10,
              fancybox=False)
    
    # Set y-axis limits to provide some padding
    ax.set_ylim(1.5, 5.0)
    
    # Set x-axis limits to provide some padding
    ax.set_xlim(-0.1, 1.1)
    
    # Tight layout for professional appearance
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('figure_2.png', 
                dpi=300, 
                bbox_inches='tight', 
                facecolor='white', 
                edgecolor='none')
    
    print("Chart saved as 'figure_2.png'")
    
    # Close the plot to free memory
    plt.close()


if __name__ == '__main__':
    create_interaction_chart()
